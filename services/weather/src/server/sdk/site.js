/**
 * @author
 * @version 0.1
 */

const SiteModel = require('../models/Site');

/*************************************************************************************************
 *   ################################   weather    ############################################  *
 *************************************************************************************************/

async function getSite() {
    return await SiteModel.find({});
}

async function addSite(name,humidity,rainPrecipitation,temperature,wind) {
    let id = 0;
    await SiteModel.create({
        "name" : name,
        "humidity": humidity,
        "rainPrecipitation": rainPrecipitation,
        "temperature": temperature,
        "wind": wind
    }).then(await async function (weather) {
        id = weather._id;
    });
    console.log(id);
    return SiteModel.findOne({'_id': id});
}

async function getSiteByName(name) {
    return await SiteModel.find({'name': name});
}


module.exports = {
    getSite,
    addSite,
    getSiteByName
};
