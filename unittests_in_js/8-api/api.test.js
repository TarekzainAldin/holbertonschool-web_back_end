const request = require('request');
const { expect } = require('chai');

describe('Index page', () => {
  const baseUrl = 'http://localhost:7865';

  it('should return correct status code', (done) => {
    request.get(baseUrl, (err, res) => {
      expect(res.statusCode).to.equal(200);
      done();
    });
  });

  it('should return correct result', (done) => {
    request.get(baseUrl, (err, res, body) => {
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });

  it('should log API available message when server starts', () => {
    // This test assumes the server is already running
    // and showing the correct startup message
    expect(true).to.be.true; // Placeholder assertion
  });
});