const mongoose = require("mongoose");
const Schema = mongoose.Schema;

//Model definition

PayloadSchema = new Schema({
    customer : {
        type: String,
        require: true
    },
    rocketName : {
        type: String,
        require: true
    },
    finalPosition : {
        type: Number,
        require: true
    },
    position : [{
        type: String
    }],
    satellite : {
        type: String,
        require: true
    },
    success  : {
        type: Boolean,
        require: true
    },
});


mongoose.model('payload', PayloadSchema);
const Payload = mongoose.model('payload');

module.exports = Payload;
