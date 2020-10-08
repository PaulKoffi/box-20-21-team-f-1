const mongoose = require("mongoose");
const Schema = mongoose.Schema;

//Model definition

RocketInventoriesSchema = new Schema({
    available  : {
        type: Boolean,
        require: true
    },
    fuel : {
        type: Number,
        require: true
    },
    speed : {
        type: Number,
        require: true
    },
    rocketName : {
        type: String,
        require: true
    }
});


mongoose.model('rocketInventories', RocketInventoriesSchema);
const RocketInventories = mongoose.model('rocketInventories');

module.exports = RocketInventories;
