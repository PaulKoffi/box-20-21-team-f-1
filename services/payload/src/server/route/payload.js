const Router = require('koa-router');
const router = new Router();
const f = require('../utils/functions');
const sdk = require('../sdk');


router.post('/payload', async (ctx) => {
    try {
        const result = await sdk.addPayload(ctx.request.body.customerName, ctx.request.body.customerMail, ctx.request.body.finalPosition, ctx.request.body.x, ctx.request.body.y, ctx.request.body.satellite);
        f.success(ctx, result);
    } catch {
        f.failure(ctx, "failed");
    }
});


router.get('/payload/payloadByRocketName/:rocketName', async (ctx) => {
    try {
        const payload = await sdk.getPayloadByRocketName(ctx.params.rocketName);
        if(payload == null){
            f.failure(ctx, "failed");
        }else {
            f.success(ctx, payload);
        }
    } catch {
        f.failure(ctx, "failed");
    }
});

router.post('/payload/setStatus', async (ctx) => {
    try {
        const result = await sdk.setStatus(ctx.request.body.rocketName);
        f.success(ctx, result);
    } catch {
        f.failure(ctx, "failed");
    }
});

module.exports = router;
