export default function hasValuesFromArray(set, arr) {
  return arr.every((element) => set.has(element));
}

// export default function hasValuesFromArray(set, arr) {
//   // Iterate through each element in the array
//   for (let i = 0; i < arr.length; i++) {
//     // Check if the set does not contain the current element
//     if (!set.has(arr[i])) {
//       return false;
//     }
//   }
//   // If all elements in the array are in the set, return true
//   return true;
// }
