/**
 * @author
 * @version 0.1
 */

const PayloadModel = require('../models/Payload');
const RocketInventoryModel = require('../models/RocketInventories');
const CustomerModel = require('../models/Customer');


/*************************************************************************************************
 *   ################################   payload    ############################################  *
 *************************************************************************************************/

async function getPayloadByRocketName(rocketName) {
    return PayloadModel.findOne({'rocketName': rocketName});
}

async function setStatus(rocketName){
    currentStatus = await getPayloadByRocketName(rocketName).success;
    await PayloadModel.updateOne({'rocketName': rocketName},{"success": !currentStatus});
}

async function addPayload(customerName, customerMail, finalPosition, x, y, satellite) {

    // Chercher une fusée Disponible
    rocketsAvailable = await RocketInventoryModel.findOne({'available': true});

    // Enregistrement du nouveau client s'il n'existe pas
    clientFound = await CustomerModel.findOne({'mail': customerMail});
    if (!clientFound) {
        await CustomerModel.create({
            "name": customerName,
            "mail": customerMail
        });
    }


    // Enregistrement Payload
    if (rocketsAvailable !== undefined) {
        await PayloadModel.create({
            "customer": customerMail,
            "rocketName": rocketsAvailable.rocketName,
            "finalPosition": finalPosition,
            "position": [String(x), String(y)],
            "satellite": satellite,
            "success": false
        });

        // rendre indisponible la rocket
        await RocketInventoryModel.updateOne({'rocketName': rocketsAvailable.rocketName},{"available" : false});
        return PayloadModel.findOne({'satellite': satellite});
    }

    return undefined;
}


module.exports = {
    addPayload,
    getPayloadByRocketName,
    setStatus
};
