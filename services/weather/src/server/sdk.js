/**
 * @author
 * @version 0.1
 */

const siteSdk = require('./sdk/site');


/******** Importations des fonctions du SDK weather *****/
const getSite = siteSdk.getSite;
const addSite = siteSdk.addSite;
const getSiteByName = siteSdk.getSiteByName;



module.exports = {
    getSite,
    addSite,
    getSiteByName
};
