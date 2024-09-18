/* eslint-disable no-undef */
const fs = require('fs');

function countStudents(path) {
  try {
    // Read the CSV file synchronously
    const data = fs.readFileSync(path, 'utf8');

    // Split the data into lines and remove any empty lines
    const lines = data.trim().split('\n').filter(line => line.length > 0);

    // Check if there are any valid lines after filtering
    if (lines.length <= 1) {
      throw new Error('Cannot load the database');
    }

    // Initialize an object to store students by field
    const studentsByField = {};

    // Process each student line starting from the second line (index 1)
    for (let i = 1; i < lines.length; i++) {
      // eslint-disable-next-line no-unused-vars
      const [firstname, lastname, age , field] = lines[i].split(',');

      // Ensure the required fields are not empty
      if (firstname && field) {
        if (!studentsByField[field]) {
          studentsByField[field] = [];
        }
        studentsByField[field].push(firstname);
      }
    }

    // Count the total number of students
    const totalStudents = Object.values(studentsByField).reduce((acc, curr) => acc + curr.length, 0);
    console.log(`Number of students: ${totalStudents}`);

    // Log students by field
    for (const field in studentsByField) {
      const studentNames = studentsByField[field].join(', ');
      console.log(`Number of students in ${field}: ${studentsByField[field].length}. List: ${studentNames}`);
    }

  } catch (error) {
    // Handle errors (file not found, etc.)
    console.error('Cannot load the database');
  }
}

module.exports = countStudents;
