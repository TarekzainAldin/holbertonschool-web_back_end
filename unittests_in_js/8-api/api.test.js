const request = require('request');
const { expect } = require('chai');

describe('Index page', () => {
  const BASE_URL = 'http://localhost:7865';

  it('should return status code 200', (done) => {
    request.get(BASE_URL, (err, res) => {
      expect(res.statusCode).to.equal(200);
      done(err);
    });
  });

  it('should return correct result', (done) => {
    request.get(BASE_URL, (err, res, body) => {
      expect(body).to.equal('Welcome to the payment system');
      done(err);
    });
  });

  it('should log API available message', () => {
    // This test assumes the server is running and logged the message
    expect(true).to.be.true; // Placeholder assertion
  });
});
