export default function updateUniqueItems(groceryMap) {
  // Vérifie si l'argument passé est une carte
  if (!(groceryMap instanceof Map)) {
    throw new Error('Cannot process'); // Impossible de traiter
  }

  // Parcourt chaque entrée de la carte
  groceryMap.forEach((quantity, item) => {
    // Si la quantité est de 1, met à jour la quantité à 100
    if (quantity === 1) { groceryMap.set(item, 100); }
  });

  return groceryMap; // Retourne la carte mise à jour
}
