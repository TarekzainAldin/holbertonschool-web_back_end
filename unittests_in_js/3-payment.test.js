const { expect } = require('chai');
const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe('sendPaymentRequestToApi function', () => {
  let utilSpy;

  beforeEach(() => {
    utilSpy = sinon.spy(Utils, 'calculateNumber');
  });

  afterEach(() => {
    utilSpy.restore();
  });

  it('validates the usage of the Utils function', () => {
    sendPaymentRequestToApi(100, 20);

    expect(utilSpy.calledOnce).to.be.true;
    expect(utilSpy.calledWith('SUM', 100, 20)).to.be.true;
  });
});
