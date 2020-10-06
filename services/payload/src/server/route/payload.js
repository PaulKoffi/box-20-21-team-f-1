const Router = require('koa-router');
const router = new Router();
const f = require('../utils/functions');
const sdk = require('../sdk');




router.post('/payload', async (ctx) => {
    try {
        const  result = await sdk.addPayload(ctx.request.body.customerName,ctx.request.body.customerMail, ctx.request.body.finalPosition,ctx.request.body.x,ctx.request.body.y,ctx.request.body.satellite);
        f.success(ctx, result);
    } catch {
        f.failure(ctx, "failed");
    }
});


router.get('/payloadByRocketName/:rocketName', async (ctx) => {
    const payload = await sdk.getPayloadByRocketName(ctx.params.rocketName);
    // console.log("Id " + users._id);
    f.success(ctx, payload);
});

module.exports = router;
