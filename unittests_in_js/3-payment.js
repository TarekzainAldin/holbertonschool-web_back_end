// 3-payment.js
import Utils from './utils.js';

function sendPaymentRequestToApi(totalAmount, totalShipping) {
  const sum = Utils.calculateNumber('SUM', totalAmount, totalShipping);
  console.log(`The total is: ${sum}`);
}

export default sendPaymentRequestToApi;
