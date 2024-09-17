const fs = require('fs').promises;

function countStudents(path) {
  return fs.readFile(path, 'utf8')
    .then((data) => {
      const lines = data.trim().split('\n').filter(line => line.length > 0);

      if (lines.length <= 1) {
        throw new Error('Cannot load the database'); // No valid data in the file
      }

      const header = lines[0].split(','); // The header row
      const studentData = lines.slice(1); // Student rows

      const students = {};
      let totalStudents = 0;

      studentData.forEach((line) => {
        const [firstname, lastname, age, field] = line.split(',');

        if (firstname && field) { // Make sure valid data is present
          if (!students[field]) {
            students[field] = [];
          }
          students[field].push(firstname);
          totalStudents += 1;
        }
      });

      // Log total number of students
      console.log(`Number of students: ${totalStudents}`);

      // Log the number of students per field
      for (const field in students) {
        const listOfStudents = students[field].join(', ');
        console.log(`Number of students in ${field}: ${students[field].length}. List: ${listOfStudents}`);
      }
    })
    .catch(() => {
      throw new Error('Cannot load the database');
    });
}

module.exports = countStudents;
