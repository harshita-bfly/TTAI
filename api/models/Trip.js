const mongoose=require("mongoose")
const TripSchema=new mongoose.Schema({
    userId: {
        type: String,
        required: true,
    },
    email:{
        type: String,
        required: true,
    },
    photo:{
        type:String,
        required:true,
    },
    startDate: {
        type: Date,
        required: true,
    },
},{timestamps:true});
module.exports=mongoose.model("Trip",TripSchema)