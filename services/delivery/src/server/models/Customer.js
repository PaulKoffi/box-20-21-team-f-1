const mongoose = require("mongoose");
const Schema = mongoose.Schema;

//Model definition

CustomerSchema = new Schema({
    name : {
        type: String,
        require: true
    },
    mail : {
        type: String,
        require: true
    }
});


mongoose.model('customer', CustomerSchema);
const Customer = mongoose.model('customer');

module.exports = Customer;
