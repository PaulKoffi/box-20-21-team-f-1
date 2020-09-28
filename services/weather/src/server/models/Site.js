const mongoose = require("mongoose");
const Schema = mongoose.Schema;

//Model definition

SiteSchema = new Schema({
    name: {
        type: String,
        required: [true, 'site name is required']
    },
    humidity : {
        type: Number,
        require: true
    },
    rainPrecipitation : {
        type: Number,
        require: true
    },
    temperature : {
        type: Number,
        require: true
    },
    wind : {
        type: Number,
        require: true
    }
});


mongoose.model('site', SiteSchema);
const Site = mongoose.model('site');

module.exports = Site;
