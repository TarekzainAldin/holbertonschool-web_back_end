const { util } = require('chai');
const sendPaymentRequestToApi = require('./3-payment');
const Utils = require('./utils');
const { utils } = require('mocha');

function sendPaymentRequestToApi(totalAmount, totalShipping){
    const sum = Utils.calculateNumber('SUM', totalAmount, totalShipping)
    console.log(`The total is : ${sum}`)
}
