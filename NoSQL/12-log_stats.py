#!/usr/bin/env python3
"""statitistiques sur les logs nginx"""


from pymongo import MongoClient


if __name__ == "__main__":
    """Fournit des statistiques sur les logs nginx"""

    # Connexion à la base de données MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client['logs']
    collection = db['nginx']

    # Liste des méthodes HTTP à analyser
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    # Affichage du nombre total de logs
    print(f"{collection.count_documents({})} logs")

    # Affichage du nombre de logs pour chaque méthode HTTP de la liste
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Affichage du nombre de logs avec méthode GET et au chemin /status
    print(collection.count_documents({"method": "GET", "path": "/status"}),
          "status check")

    # Fermeture de la connexion à la base de données MongoDB
    client.close()
