/* eslint-disable no-undef */
// full_server/controllers/AppController.js

export class AppController {
    static getHomepage(req, res) {
      return res.status(200).send('Hello Holberton School!');
    }
  }
  
module.exports = AppController;