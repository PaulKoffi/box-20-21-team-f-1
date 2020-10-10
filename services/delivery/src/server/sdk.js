/**
 * @author
 * @version 0.1
 */

const payloadSdk = require('./sdk/payload');


/******** Importations des fonctions du SDK payload *****/
const addPayload = payloadSdk.addPayload;
const getPayloadByRocketName = payloadSdk.getPayloadByRocketName;
const setStatus = payloadSdk.setStatus;
const getPayloadBySatelliteName = payloadSdk.getPayloadBySatelliteName;






module.exports = {
    addPayload,
    getPayloadByRocketName,
    setStatus,
    getPayloadBySatelliteName
};
