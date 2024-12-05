import requests

# URL du serveur Flask
url = "http://127.0.0.1:5000/upload"  # Remplacez par l'URL de votre serveur Flask

# Nom du fichier à envoyer
file_path = "message.txt"

# Crée un fichier texte pour tester
with open(file_path, "w") as file:
    file.write("Ceci est un fichier texte envoyé via une méthode POST en Python.")

# Envoi du fichier via une requête POST
try:
    with open(file_path, "rb") as file:
        files = {"file": (file_path, file)}
        response = requests.post(url, files=files)
    
    if response.status_code == 200:
        print("Fichier envoyé avec succès :", response.text)
    else:
        print("Échec de l'envoi. Code de statut :", response.status_code)
        print("Réponse du serveur :", response.text)

except Exception as e:
    print("Une erreur est survenue :", e)