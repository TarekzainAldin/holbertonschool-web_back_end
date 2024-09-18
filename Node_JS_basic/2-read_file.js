#!/usr/bin/env node
/* eslint-disable no-undef */
// eslint-disable-next-line no-undef
const fs = require('fs');

function countStudents(path) {
  try {
    // Read the CSV file synchronously
    const data = fs.readFileSync(path, 'utf8');

    // Split the content into lines and remove empty lines
    const lines = data.trim().split('\n').filter(line => line.length > 0);

    // Ensure there is at least a header and some data
    if (lines.length <= 1) {
      throw new Error('Cannot load the database');
    }

    // Remove the header row
    const studentData = lines.slice(1);

    const students = {};
    let totalStudents = 0;

    // Loop through each line and process student data
    for (const line of studentData) {
      const [firstname, , , field] = line.split(',');

      // Check that necessary fields (firstname and field) are not empty
      if (firstname && field) {
        if (!students[field]) {
          students[field] = [];
        }
        students[field].push(firstname);
        totalStudents += 1;
      }
    }

    // Output the total number of students
    console.log(`Number of students: ${totalStudents}`);

    // Output the number of students in each field with their first names
    for (const field in students) {
      const listOfStudents = students[field].join(', ');
      console.log(`Number of students in ${field}: ${students[field].length}. List: ${listOfStudents}`);
    }

  } catch (error) {
    // Catch any error and log the specific message
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
