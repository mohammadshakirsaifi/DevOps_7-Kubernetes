const express = require("express");
const app = express();

app.get("/", (req, res) => {
  res.json({ message: "Hello from Express Backend!" });
});

app.listen(3000, () => {
  console.log("Express server running on port 3000");
});
