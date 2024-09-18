/* eslint-disable no-undef */
// full_server/server.js

import express from 'express';
import routes from './routes/index.js';

const app = express();
const PORT = 1245;

app.use(express.json());
app.use(routes);

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});

export default app;
module.exports = app;
