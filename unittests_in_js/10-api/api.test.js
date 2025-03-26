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
  });

  describe('Available payments', () => {
    it('should return status code 200', (done) => {
      request.get(`${BASE_URL}/available_payments`, (err, res) => {
        expect(res.statusCode).to.equal(200);
        done(err);
      });
    });

    it('should return correct payment methods object', (done) => {
      request.get(`${BASE_URL}/available_payments`, (err, res, body) => {
        const expected = {
          payment_methods: {
            credit_cards: true,
            paypal: false
          }
        };
        expect(JSON.parse(body)).to.deep.equal(expected);
        done(err);
      });
    });
  });

  describe('Login', () => {
    it('should return status code 200', (done) => {
      const options = {
        url: `${BASE_URL}/login`,
        method: 'POST',
        json: { userName: 'Betty' }
      };
      request(options, (err, res) => {
        expect(res.statusCode).to.equal(200);
        done(err);
      });
    });

    it('should return correct welcome message', (done) => {
      const options = {
        url: `${BASE_URL}/login`,
        method: 'POST',
        json: { userName: 'Betty' }
      };
      request(options, (err, res, body) => {
        expect(body).to.equal('Welcome Betty');
        done(err);
      });
    });
  });
});