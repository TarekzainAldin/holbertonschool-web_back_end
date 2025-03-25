export default function calculateNumber(type, a, b) {
	const numA = Math.round(a);
	const numB = Math.round(b);
  
	if (type === "SUM") {
	  return numA + numB;
	} else if (type === "SUBTRACT") {
	  return numA - numB;
	} else if (type === "DIVIDE") {
	  if (numB === 0) return "Error";
	  return numA / numB;
	} else {
	  throw new Error("Invalid operation type");
	}
  }
  