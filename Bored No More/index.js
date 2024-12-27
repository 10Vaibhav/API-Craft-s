import express from "express";
import bodyParser from "body-parser";
import axios from "axios";

const app = express();
const port = 3000;

app.use(express.static("public"));
app.use(bodyParser.urlencoded({ extended: true }));

app.get("/", async (req, res) => {
  try {
    const request = await axios.get("https://bored-api.appbrewery.com/random");
    const data = request.data;


    res.render("index.ejs", { activity:  data });
  } catch (error) {
    res.render("index.ejs", {
      error_Message: error.message,
    });
  }
});

app.post("/", async (req, res) => {
  console.log(req.body);

  const type = req.body.type;
  const participants = req.body.participants;

  try {
    const request = await axios.get(`https://bored-api.appbrewery.com/filter?type=${type}&participants=${participants}`);

    const data = request.data;
    console.log(data);

    res.render("index.ejs", { activity: data[Math.floor(Math.random() * data.length)]});
  } catch (error) {
    res.render("index.ejs", {
      error_Message: "No activities that match your criteria.",
    });
  }
});

app.listen(port, () => {
  console.log(`Server running on port: ${port}`);
});
