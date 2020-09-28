const Koa = require('koa');
const cors = require('@koa/cors');
const bodyParser = require('koa-bodyparser');
const mongoose = require('mongoose');
const logger = require('koa-logger');
const config = require('./config');
const sdk = require('./src/server/sdk');


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


module.exports = {
    server
};


