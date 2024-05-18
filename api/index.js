const express=require("express")
const app=express()
const mongoose=require("mongoose")
const tripRoute=require("./routes/trip")
const dotenv=require("dotenv")
dotenv.config()
mongoose.connect(process.env.MONGO_URL,{
    useNewUrlParser:true,
    useUnifiedTopology:true,
}).then(()=>console.log("Connected")).catch("Error")

app.use(express.json());
app.use("/api/trip",tripRoute);

app.listen(8800,()=>{
    console.log("Backend is running")
})