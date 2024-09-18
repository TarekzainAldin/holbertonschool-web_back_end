#!/usr/bin/env node
/* eslint-disable no-undef */
const express = require('express');
const fs = require('fs');
const app = express();
const PORT = 1245;

// Function to read and count students from a CSV file asynchronously
const countStudentsFromCSV = (path) => {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        return reject(new Error('Cannot load the database'));
      }
      const lines = data.trim().split('\n').filter(line => line.length > 0);
      if (lines.length <= 1) {
        return reject(new Error('Cannot load the database'));
      }
      const studentsByField = {};
      for (let i = 1; i < lines.length; i++) {
        // eslint-disable-next-line no-unused-vars
        const [firstname, lastname, age, field] = lines[i].split(',').map(item => item.trim());
        if (firstname && field) {
          if (!studentsByField[field]) {
            studentsByField[field] = [];
          }
          studentsByField[field].push(firstname);
        }
      }
      const totalStudents = Object.values(studentsByField).reduce((acc, curr) => acc + curr.length, 0);
      const response = [`Number of students: ${totalStudents}`];
      for (const field in studentsByField) {
        response.push(`Number of students in ${field}: ${studentsByField[field].length}. List: ${studentsByField[field].join(', ')}`);
      }
      resolve(response.join('\n'));
    });
  });
};

// Root endpoint
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

// Students endpoint
app.get('/students', async (req, res) => {
  try {
    const result = await countStudentsFromCSV(process.argv[2]);
    res.send(`This is the list of our students\n${result}`);
  } catch (error) {
    res.status(500).send(error.message);
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});

// Export the app variable
module.exports = app;
