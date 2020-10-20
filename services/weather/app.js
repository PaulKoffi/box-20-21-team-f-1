const Koa = require('koa');
const cors = require('@koa/cors');
const bodyParser = require('koa-bodyparser');
const mongoose = require('mongoose');
const logger = require('koa-logger');
const config = require('./config');
const sdk = require('./src/server/sdk');
const { Kafka } = require('kafkajs');

const siteRoute  = require('./src/server/route/site');

const app = new Koa();
const PORT = 3000;

app.use(bodyParser());
app.use(logger());
app.use(cors({origin: '*', exposeHeaders: '*'}));
app.use(siteRoute.routes());

mongoose.connect(`mongodb+srv://${config.configDB.userName}:${config.configDB.password}@${config.configDB.host}/${config.configDB.name}?retryWrites=true&w=majority`, {
    useNewUrlParser: true,
    useCreateIndex: true
});

mongoose.set('debug', true);

const server = app.listen(PORT, () => {
    console.log(`Server listening on port: ${PORT}`);
});

                                                 //  ######### KAFKA ######## //
const kafka = new Kafka({
    clientId: 'weather-node',
    brokers: ['localhost:9092']
});

const producer = kafka.producer();
const consumer = kafka.consumer({ groupId: 'weather-group' });

const run = async () => {
    // Producing
    await producer.connect();

    // Consuming
    await consumer.connect();
    await consumer.subscribe({ topic: 'Pollrequesttopic', fromBeginning: true });

    await consumer.run({
        eachMessage: async ({ topic, partition, message }) => {
            console.log("ici");
            console.log({
                partition,
                offset: message.offset,
                value: message.value.toString()
            });


            if (message.value.toString() === "sites") {
                const weather = await sdk.getSite();
                await producer.send({
                    topic: 'pollresponsetopic',
                    messages: [
                        { value: JSON.stringify(weather) },
                    ],
                });
            } else {
                const weather = await sdk.getSiteByName(message.value.toString());
                await producer.send({
                    topic: 'pollresponsetopic',
                    messages: [
                        { value: JSON.stringify(weather) },
                    ],
                });
            }
        },
    })
};

run().catch(console.error);

module.exports = {
    server
};


