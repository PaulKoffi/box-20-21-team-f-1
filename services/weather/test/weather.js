// let chai = require('chai');
// let chaiHttp = require('chai-http');
// var assert = require('assert');
// const sdk = require('../src/server/sdk');
//
// process.env.NODE_ENV = 'test';
//
// const server = require('../app');
//
// chai.use(chaiHttp);
//
// describe('endpoints test', async () => {
//
//     describe('/POST new Site', async () => {
//         it('add new Site to mongoDB', (done) => {
//             let weather = {
//                 "name": "Nice",
//                 "humidity": 2,
//                 "rainPrecipitation": 3  ,
//                 "temperature": 7,
//                 "wind": 9
//             };
//
//             chai.request(server)
//                 .post('/site')
//                 .send(weather)
//                 .end(async (err, res) => {
//                     // assert.strictEqual(2, siteFind.humidity);
//                     //res.status.should.be.equal(200);
//                     console.table(res.text);
//                     //:const siteFind = await sdk.getSiteByName("Nice");
//                     assert.strictEqual(2, res.text.humidity);
//                     //done();
//                 });
//         });
//
//     });
//
// });