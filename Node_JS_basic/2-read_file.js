const fs = require('fs');

function countStudents(path) {
  try {
    // Read the CSV file synchronously
    const data = fs.readFileSync(path, 'utf8');

    // Split the content into lines and remove empty lines
    const lines = data.trim().split('\n').filter(line => line.length > 0);

    if (lines.length <= 1) {
      throw new Error('Cannot load the database'); // No valid data in the file
    }

    // Remove the header row (first line)
    const header = lines[0].split(',');
    const studentData = lines.slice(1);

    const students = {};
    let totalStudents = 0;

    // Loop through each line and process student data
    for (const line of studentData) {
      const [firstname, lastname, age, field] = line.split(',');

      if (firstname && field) {  // Check that necessary fields are not empty
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
    console.error('Cannot load the database');
  }
}

module.exports = countStudents;
