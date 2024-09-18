/* eslint-disable no-undef */
// full_server/controllers/StudentsController.js

import { readDatabase } from '../utils.js';

export class StudentsController {
  static async getAllStudents(req, res) {
    try {
      const students = await readDatabase('./database.csv');
      const fields = Object.keys(students).sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()));
      
      let response = 'This is the list of our students\n';
      fields.forEach(field => {
        response += `Number of students in ${field}: ${students[field].length}. List: ${students[field].join(', ')}\n`;
      });

      return res.status(200).send(response);
    } catch (error) {
      return res.status(500).send('Cannot load the database');
    }
  }

  static async getAllStudentsByMajor(req, res) {
    const { major } = req.params;

    if (!['CS', 'SWE'].includes(major)) {
      return res.status(500).send('Major parameter must be CS or SWE');
    }

    try {
      const students = await readDatabase('./database.csv');
      if (!students[major]) {
        return res.status(500).send('Cannot load the database');
      }
      return res.status(200).send(`List: ${students[major].join(', ')}`);
    } catch (error) {
      return res.status(500).send('Cannot load the database');
    }
  }
}
module.exports = StudentsController;