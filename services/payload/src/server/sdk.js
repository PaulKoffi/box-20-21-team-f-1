/**
 * @author
 * @version 0.1
 */

const payloadSdk = require('./sdk/payload');


/******** Importations des fonctions du SDK payload *****/
const addPayload = payloadSdk.addPayload;
const getPayloadByRocketName = payloadSdk.getPayloadByRocketName;




module.exports = {
    addPayload,
    getPayloadByRocketName
};
