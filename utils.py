#!/usr/bin/env python3
"""
utils.py

Simple helper to draw red rectangles around boxes on an image and save it.
"""
from PIL import Image, ImageDraw

def draw_boxes(input_image_path, boxes, output_image_path):
    """
    Open the image at input_image_path, draw a red rectangle for each box,
    and save to output_image_path.

    boxes : list of boxes, each box is [x1, y1, x2, y2]
    """
    with Image.open(input_image_path) as img:
        draw = ImageDraw.Draw(img)

        outline_color = (255, 0, 0)  # red
        line_width = 3

        for box in boxes:
            try:
                x1, y1, x2, y2 = box
                rect = [int(x1), int(y1), int(x2), int(y2)]
                # Use width if Pillow supports it; otherwise it will still work in recent versions.
                draw.rectangle(rect, outline=outline_color, width=line_width)
            except Exception:
                # Skip malformed boxes
                continue

        img.save(output_image_path)
