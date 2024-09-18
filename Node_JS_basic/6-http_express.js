/* eslint-disable no-undef */
// Import the express module
const express = require('express');

// Initialize the Express application
const app = express();

// Define a route for the root URL
app.get('/', (req, res) => {
  res.send('Hello Holberton School!'); // Send the response
});

// Make the app listen on port 1245
const PORT = 1245;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

// Export the app for use in other modules
module.exports = app;
