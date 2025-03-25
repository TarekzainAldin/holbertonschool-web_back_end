const assert = require("assert");
const calculateNumber = require("./0-calcul");

describe("calculateNumber", () => {
  it("should return the sum of two rounded numbers", () => {
    assert.strictEqual(calculateNumber(1, 3), 4);
    assert.strictEqual(calculateNumber(1, 3.7), 5);
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
    assert.strictEqual(calculateNumber(2.6, 2.4), 5);
  });

  it("should handle negative numbers correctly", () => {
    assert.strictEqual(calculateNumber(-1.4, -3.6), -5);
    assert.strictEqual(calculateNumber(-1.5, -3.6), -5);
  });

  it("should handle mixed sign numbers", () => {
    assert.strictEqual(calculateNumber(-1.4, 3.6), 3);
    assert.strictEqual(calculateNumber(1.4, -3.6), -2);
  });

  it("should handle zeros correctly", () => {
    assert.strictEqual(calculateNumber(0, 0), 0);
    assert.strictEqual(calculateNumber(0, 4.5), 5);
  });
});
