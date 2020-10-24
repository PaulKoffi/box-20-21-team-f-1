const Koa = require('koa');
const cors = require('@koa/cors');
const bodyParser = require('koa-bodyparser');
const mongoose = require('mongoose');
const logger = require('koa-logger');
const config = require('./config');
const sdk = require('./src/server/sdk');
const { Kafka } = require('kafkajs');
const Router = require('koa-router');
const router = new Router();
const f = require('./src/server/utils/functions');


//  ######### KAFKA ######## //
const kafka = new Kafka({
    clientId: 'my-app',
    brokers: ['localhost:9092']
});

const producer = kafka.producer();
const consumer = kafka.consumer({ groupId: 'weather-group' });
const consumer1 = kafka.consumer({ groupId: 'weath-group' });

const run = async () => {
    // Producing
    // await producer.connect();
    // Consuming
    await consumer.connect();
    await consumer.subscribe({ topic: 'Pollrequest-topic', fromBeginning: true });

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
                    topic: 'polltoryresponsetopic',
                    messages: [
                        { value:JSON.stringify(weather)}
                    ],
                });
            } else {
                siteName = JSON.parse(message.value.toString())['siteName'];
                const weather = await sdk.getSiteByName(siteName);
                await producer.send({
                    topic: 'polltoryresponsetopic',
                    messages: [
                        { value: JSON.stringify({'response': JSON.stringify(weather), 'request': message.value.toString() }) },
                    ],
                });
            }
        }
    })



    await consumer1.connect();
    await consumer1.subscribe({ topic: 'pollresponsetopic', fromBeginning: true });

    await consumer1.run({
        eachMessage: async ({ topic, partition, message }) => {
            console.log("II");
            console.log({
                partition,
                offset: message.offset,
                value: message.value.toString()
            });

        }
    })
};

run().catch(console.error);

router.get('/', async (ctx) => {
    await producer.connect()
    await producer.send({
        topic: 'Pollrequest-topic',
        messages: [
            { value: 'sites' },
        ],
    });
    f.failure(ctx, "failed");
});


const siteRoute  = require('./src/server/route/site');

const app = new Koa();
const PORT = 3000;

app.use(bodyParser());
app.use(logger());
app.use(cors({origin: '*', exposeHeaders: '*'}));
app.use(siteRoute.routes());
app.use(router.routes());


mongoose.connect(`mongodb+srv://${config.configDB.userName}:${config.configDB.password}@${config.configDB.host}/${config.configDB.name}?retryWrites=true&w=majority`, {
    useNewUrlParser: true,
    useCreateIndex: true
});

mongoose.set('debug', true);

const server = app.listen(PORT, () => {
    console.log(`Server listening on port: ${PORT}`);
});



module.exports = {
    server
};


