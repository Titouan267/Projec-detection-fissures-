#!/usr/bin/env python3
"""
inference.py

Usage:
    python inference.py image.jpg

Simple script qui envoie une image à une API d'inférence, affiche la réponse
JSON et dessine des rectangles rouges autour des boxes retournées.
Remplacez API_URL par l'URL de votre modèle.
"""
import sys
import os
import json
import requests
from utils import draw_boxes

# Remplacez cette URL par l'URL de votre API d'inférence
API_URL = "https://your-api-url.example/predict"

def send_image_for_inference(image_path, api_url):
    """
    Envoie l'image à l'API via multipart/form-data et retourne le JSON réponse.
    On suppose que l'API accepte le champ 'image' pour le fichier.
    """
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Fichier introuvable: {image_path}")

    with open(image_path, "rb") as f:
        files = {"image": (os.path.basename(image_path), f, "image/jpeg")}
        try:
            resp = requests.post(api_url, files=files, timeout=30)
        except requests.RequestException as e:
            raise RuntimeError(f"Erreur lors de la requête HTTP : {e}")

    if resp.status_code != 200:
        raise RuntimeError(f"API a répondu avec le statut {resp.status_code}: {resp.text}")

    try:
        data = resp.json()
    except json.JSONDecodeError:
        raise RuntimeError(f"La réponse de l'API n'est pas du JSON valide: {resp.text}")

    return data

def main():
    if len(sys.argv) < 2:
        print("Usage: python inference.py image.jpg")
        sys.exit(1)

    image_path = sys.argv[1]
    output_path = "output.jpg"

    # Envoi de l'image à l'API
    print(f"Envoi de l'image '{image_path}' à l'API ({API_URL})...")
    try:
        result = send_image_for_inference(image_path, API_URL)
    except Exception as e:
        print("Erreur :", e)
        sys.exit(1)

    # Affichage de la réponse JSON
    print("Réponse JSON reçue de l'API :")
    print(json.dumps(result, indent=2, ensure_ascii=False))

    # Récupération des boxes attendues dans le format indiqué par l'utilisateur
    # Exemple attendu: { "boxes": [[x1,y1,x2,y2], ...], "scores": [0.95, ...] }
    boxes = result.get("boxes", [])
    if not isinstance(boxes, list):
        print("Attention : 'boxes' n'est pas une liste. Rien à dessiner.")
        boxes = []

    # Dessine et sauvegarde l'image de sortie
    try:
        draw_boxes(image_path, boxes, output_path)
        print(f"Image résultat sauvegardée dans '{output_path}'.")
    except Exception as e:
        print("Erreur lors du dessin des boxes :", e)
        sys.exit(1)

if __name__ == "__main__":
    main()
