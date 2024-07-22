export default function createInt8TypedArray(length, position, value) {
  // Create an ArrayBuffer with the specified length
  const buffer = new ArrayBuffer(length);

  // Create a DataView for the buffer
  const view = new DataView(buffer);

  // Check if the position is within bounds
  if (position < 0 || position >= length) {
    throw new Error('Position outside range'); // Position out of bounds
  }

  // Set the Int8 value at the specified position
  view.setInt8(position, value);

  return view;
}
