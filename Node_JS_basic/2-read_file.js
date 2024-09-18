#!/usr/bin/env node
/* eslint-disable no-undef */

const fs = require('fs');

function countStudents (path) {
  try {
    const data = fs.readFileSync(path, 'utf8');
    const lines = data.trim().split('\n');

    const students = [];

    for (const line of lines) {
      const [firstname, lastname, age, field] = line.split(',');
      if (firstname && lastname && age && field && field !== 'field') {
        students.push({
          firstname, lastname, age, field
        });
      }
    }

    const studentCount = students.length;
    console.log(`Number of students: ${studentCount}`);

    const fields = {};

    for (const student of students) {
      if (!fields[student.field]) {
        fields[student.field] = [];
      }
      fields[student.field].push(student.firstname);
    }

    for (const field in fields) {
      if (Object.prototype.hasOwnProperty.call(fields, field)) {
        console.log(`Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`);
      }
    }
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;