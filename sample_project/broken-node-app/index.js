// This application demonstrates a common "Module Not Found" error.
// The developer forgot to add 'express' to the package.json dependencies.

const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => {
  res.send('Hello TraceAI!');
});

app.listen(port, () => {
  console.log(`Sample app listening at http://localhost:${port}`);
});
