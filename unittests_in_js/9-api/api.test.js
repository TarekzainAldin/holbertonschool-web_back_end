const request = require('request');
const { expect } = require('chai');

describe('API tests', () => {
  const BASE_URL = 'http://localhost:7865';

  describe('Index page', () => {
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
  });

  describe('Cart page', () => {
    it('should return status code 200 when :id is a number', (done) => {
      request.get(`${BASE_URL}/cart/12`, (err, res) => {
        expect(res.statusCode).to.equal(200);
        done(err);
      });
    });

    it('should return correct result when :id is a number', (done) => {
      request.get(`${BASE_URL}/cart/12`, (err, res, body) => {
        expect(body).to.equal('Payment methods for cart 12');
        done(err);
      });
    });

    it('should return status code 404 when :id is NOT a number', (done) => {
      request.get(`${BASE_URL}/cart/hello`, (err, res) => {
        expect(res.statusCode).to.equal(404);
        done(err);
      });
    });

    it('should return correct error message when :id is NOT a number', (done) => {
      request.get(`${BASE_URL}/cart/hello`, (err, res, body) => {
        expect(body).to.include('Cannot GET /cart/hello');
        done(err);
      });
    });
  });
});
