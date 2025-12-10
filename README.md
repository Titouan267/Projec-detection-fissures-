# Détection de fissures - démonstration simple

Ce petit projet montre un pipeline d'inférence minimal en Python : il envoie une image à une API d'inférence (votre modèle déjà hébergé ailleurs), récupère des boxes (coordonnées de détections) et dessine des rectangles rouges sur l'image pour illustrer les résultats.

Fichiers fournis
- `inference.py` : script principal. Usage : `python inference.py image.jpg`
- `utils.py` : contient la fonction `draw_boxes` qui dessine et sauvegarde l'image de sortie.
- `README.md` : ce fichier.

Installation (prérequis)
- Python 3
- Installer les librairies requises :
  - requests
  - pillow

Exemple d'installation :
```
pip install requests pillow
```

Comment utiliser
1. Remplacez l'URL de l'API dans `inference.py` :
   - Ouvrez `inference.py` et modifiez la variable `API_URL` en haut du fichier.
   - Exemple :
     ```
     API_URL = "https://mon-serveur.example/api/predict"
     ```

2. Lancez l'inférence sur une image :
```
python inference.py image.jpg
```
- Le script :
  - enverra `image.jpg` à l'API,
  - affichera la réponse JSON dans le terminal,
  - dessinera un rectangle rouge autour de chaque box retournée,
  - sauvegardera l'image annotée sous le nom `output.jpg`.

Format attendu de la réponse de l'API
- Le script attend un JSON de la forme (exemple) :
```json
{
  "boxes": [[x1, y1, x2, y2], [x1, y1, x2, y2]],
  "scores": [0.95, 0.87]
}
```
- Seul le champ `boxes` est utilisé par le script pour dessiner les rectangles. Les coordonnées doivent être en pixels, avec (0,0) en haut à gauche.

Notes et limitations
- Ce projet est une démonstration simple pour un travail scolaire. Il ne comporte pas de gestion avancée des erreurs ni d'authentification pour l'API.
- Si votre API attend un nom de champ différent que `image` pour le fichier, adaptez la fonction `send_image_for_inference` dans `inference.py`.

Bonne démonstration !
