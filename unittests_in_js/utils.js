const Utils = {
    calculateNumber(type, a, b) {
      const numA = Math.round(a);
      const numB = Math.round(b);
  
      if (type === 'SUM') return numA + numB;
      if (type === 'SUBTRACT') return numA - numB;
      if (type === 'DIVIDE') return numB === 0 ? 'Error' : numA / numB;
  
      throw new TypeError('Invalid operation type');
    }
  };
  
  export default Utils;
  