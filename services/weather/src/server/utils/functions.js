// sets the params of the response when the request was successfully completed
function success(ctx, data) {
    ctx.status = 200;
    if (data) {
        ctx.body = data;
    } else {
        ctx.body = 'Ok';
    }
}

function failure(ctx, data) {
    ctx.status = 403;
    ctx.body = data;
}

function failure409(ctx, data) {
    ctx.status = 409;
    ctx.body = data;
}

function failure408(ctx, data) {
    ctx.status = 408;
    ctx.body = data;
}

module.exports = {
    success,
    failure,
    failure409,
    failure408
};
