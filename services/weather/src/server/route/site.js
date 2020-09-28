const Router = require('koa-router');
const router = new Router();
const f = require('../utils/functions');
const sdk = require('../sdk');

router.get('/site', async (ctx) => {
    try {
        const weather = await sdk.getSite();
        f.success(ctx, weather);
    } catch {
        f.failure(ctx, "failed");
    }
});

router.post('/site', async (ctx) => {
    try {
        const weather = await sdk.addSite(ctx.request.body.name,ctx.request.body.humidity, ctx.request.body.rainPrecipitation,ctx.request.body.temperature,ctx.request.body.wind);
        f.success(ctx, weather);
    } catch {
        f.failure(ctx, "failed");
    }
});

router.get('/siteByName/:name', async (ctx) => {
    try {
        const weather = await sdk.getSiteByName(ctx.params.name);
        f.success(ctx, weather);
    } catch {
        f.failure(ctx, "failed");
    }
});



module.exports = router;
