export default function updateUniqueItems(groceryMap) {
    // Check if the argument passed is a Map
    if (!(groceryMap instanceof Map)) {
      throw new Error('Cannot process'); // Cannot process
    }
  
    // Iterate over each entry in the map
    groceryMap.forEach((quantity, item) => {
      // If the quantity is 1, update the quantity to 100
      if (quantity === 1) {
        groceryMap.set(item, 100);
      }
    });
  
    return groceryMap; // Return the updated map
  }
  