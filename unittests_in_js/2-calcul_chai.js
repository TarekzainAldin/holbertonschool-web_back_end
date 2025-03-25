// 2-calcul_chai.js
export function calculateNumber(type, a, b) {
	let aRounded = Math.round(a);
	let bRounded = Math.round(b);
  
	if (type === "SUM") {
	  return aRounded + bRounded;
	}
	if (type === "SUBTRACT") {
	  return aRounded - bRounded;
	}
	if (type === "DIVIDE") {
	  if (bRounded === 0) {
		return "Error";
	  }
	  return aRounded / bRounded;
	}
  }
  