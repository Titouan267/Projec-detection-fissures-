#!/usr/bin/env python3
"""
utils.py

Fonction simple pour dessiner des rectangles rouges autour de boxes
sur une image et sauvegarder le résultat.
"""
from PIL import Image, ImageDraw

def draw_boxes(input_image_path, boxes, output_image_path):
    """
    Ouvre l'image à input_image_path, dessine un rectangle rouge pour chaque box
    et sauvegarde dans output_image_path.

    boxes : liste de boxes, chaque box est [x1, y1, x2, y2]
    """
    # Ouvrir l'image
    with Image.open(input_image_path) as img:
        draw = ImageDraw.Draw(img)

        # Paramètres visuels
        outline_color = (255, 0, 0)  # rouge
        line_width = 3

        # Dessiner chaque box
        for box in boxes:
            # S'assurer que la box contient 4 valeurs numériques
            try:
                x1, y1, x2, y2 = box
                # Convertir en int pour Pillow
                rect = [int(x1), int(y1), int(x2), int(y2)]
                # Pillow >= 5.0 accepte width, sinon on peut tracer plusieurs rectangles.
                draw.rectangle(rect, outline=outline_color, width=line_width)
            except Exception:
                # Ignorer les boxes mal formées
                continue

        # Sauvegarder l'image résultante
        img.save(output_image_path)
