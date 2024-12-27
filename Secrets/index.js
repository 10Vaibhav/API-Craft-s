import express from "express";
import axios from "axios";
import bodyParser from "body-parser";

const app = express();
const port = 3000;

app.use(express.static("public"));
app.use(bodyParser.urlencoded({extended: true}));

app.get("/", async(req,res)=>{

    try{

        const response = await axios.get("https://secrets-api.appbrewery.com/random");

        const data = response.data;

        res.locals.secret = data.secret;
        res.locals.user = data.username;

        res.render("index.ejs")

    }catch(error) {
        console.log(error.message)
    }

})

app.listen(port, ()=>{
    console.log(`Server is Running on port ${port}.`)
})

