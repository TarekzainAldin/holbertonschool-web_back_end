// 3-payment.test.js
import sinon from 'sinon';
import { expect } from 'chai';
import Utils from './utils.js';
import sendPaymentRequestToApi from './3-payment.js';

describe('sendPaymentRequestToApi', () => {
  it('should call Utils.calculateNumber with SUM and correct arguments', () => {
    const calculateNumberSpy = sinon.spy(Utils, 'calculateNumber');
    sendPaymentRequestToApi(100, 20);
    
    expect(calculateNumberSpy.calledOnce).to.be.true;
    expect(calculateNumberSpy.calledWith('SUM', 100, 20)).to.be.true;
    calculateNumberSpy.restore();
  });

  it('should log the correct total to console', () => {
    const calculateNumberStub = sinon.stub(Utils, 'calculateNumber').returns(120);
    const consoleSpy = sinon.spy(console, 'log');
    
    sendPaymentRequestToApi(100, 20);
    
    expect(consoleSpy.calledWith('The total is: 120')).to.be.true;
    calculateNumberStub.restore();
    consoleSpy.restore();
  });
});
