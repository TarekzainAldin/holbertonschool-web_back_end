/* eslint-disable no-unused-vars */
/* eslint-disable no-undef */
const express = require('express');
const fs = require('fs');

// Initialize the Express application
const app = express();

// Function to read students from the database
const countStudents = (path) => {
  try {
    // Read the CSV file synchronously
    const data = fs.readFileSync(path, 'utf8');
    const lines = data.trim().split('\n').filter(line => line.length > 0);

    if (lines.length <= 1) {
      return 'Cannot load the database';
    }

    const studentsByField = {};

    for (let i = 1; i < lines.length; i++) {
      const [firstname, lastname, age, field] = lines[i].split(',');
      if (firstname && field) {
        if (!studentsByField[field]) {
          studentsByField[field] = [];
        }
        studentsByField[field].push(firstname);
      }
    }

    const totalStudents = Object.values(studentsByField).reduce((acc, curr) => acc + curr.length, 0);
    let response = `Number of students: ${totalStudents}\n`;

    for (const field in studentsByField) {
      const studentNames = studentsByField[field].join(', ');
      response += `Number of students in ${field}: ${studentsByField[field].length}. List: ${studentNames}\n`;
    }

    return response.trim(); // Trim to remove extra newline at the end
  } catch (error) {
    return 'Cannot load the database';
  }
};

// Define a route for the root URL
app.get('/', (req, res) => {
  res.send('Hello Holberton School!'); // Send the response for the root path
});

// Define a route for /students
app.get('/students', (req, res) => {
  const dbPath = 'path/to/your/database.csv'; // Update this path to your CSV file
  const studentList = countStudents(dbPath);
  res.send(`This is the list of our students\n${studentList}`);
});

// Make the app listen on port 1245
const PORT = 1245;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

// Export the app for use in other modules
module.exports = app;
