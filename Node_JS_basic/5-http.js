const http = require('http');
const fs = require('fs').promises;
const url = require('url');

// Function to read and process the CSV file asynchronously
function countStudents(path) {
  return fs.readFile(path, 'utf8')
    .then((data) => {
      const lines = data.trim().split('\n').filter(line => line.length > 0);

      if (lines.length <= 1) {
        throw new Error('Cannot load the database');
      }

      const studentData = lines.slice(1); // Skip header row
      const students = {};
      let totalStudents = 0;

      studentData.forEach((line) => {
        const [firstname, lastname, age, field] = line.split(',');

        if (firstname && field) { // Ensure valid data
          if (!students[field]) {
            students[field] = [];
          }
          students[field].push(firstname);
          totalStudents += 1;
        }
      });

      // Generate the result to be returned
      let result = `Number of students: ${totalStudents}\n`;

      for (const field in students) {
        const listOfStudents = students[field].join(', ');
        result += `Number of students in ${field}: ${students[field].length}. List: ${listOfStudents}\n`;
      }

      return result.trim(); // Return the formatted result
    })
    .catch(() => {
      throw new Error('Cannot load the database');
    });
}

// Create the HTTP server and assign it to the 'app' variable
const app = http.createServer((req, res) => {
  const parsedUrl = url.parse(req.url, true);

  if (parsedUrl.pathname === '/') {
    // For the root endpoint "/"
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello Holberton School!');
  } else if (parsedUrl.pathname === '/students') {
    // For the "/students" endpoint
    const databasePath = process.argv[2]; // Get the database path from command-line arguments

    countStudents(databasePath)
      .then((studentList) => {
        res.writeHead(200, { 'Content-Type': 'text/plain' });
        res.end(`This is the list of our students\n${studentList}`);
      })
      .catch((err) => {
        res.writeHead(500, { 'Content-Type': 'text/plain' });
        res.end(err.message);
      });
  } else {
    // For any other endpoint, return a 404
    res.writeHead(404, { 'Content-Type': 'text/plain' });
    res.end('Not Found');
  }
});

// The server should listen on port 1245
app.listen(1245, () => {
  console.log('Server is running on port 1245');
});

// Export the 'app' variable (the server)
module.exports = app;
