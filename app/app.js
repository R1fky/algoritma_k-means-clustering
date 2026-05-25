import express from "express";
import clusterRouter from "./router/clusterRouter.js";

const app = express();
app.use(express.json());
const port = 3000;

app.get("/", (req, res) => {
  res.send("First API");
});

app.use("/predicts", clusterRouter);

app.listen(port, () => {
  console.log(`server running in http://localhost:${port}`);
});
