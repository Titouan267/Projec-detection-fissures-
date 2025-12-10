#!/usr/bin/env python3
"""
inference.py

Usage:
    python inference.py image.jpg

Simple script that sends an image to an inference API, prints the JSON
response and draws red rectangles around returned boxes.
Replace API_URL with your model's URL.
"""
import sys
import os
import json
import requests
from utils import draw_boxes

# Replace this URL with your inference API URL
API_URL = "https://your-api-url.example/predict"

def send_image_for_inference(image_path, api_url):
    """
    Send the image to the API using multipart/form-data and return the JSON response.
    This assumes the API accepts the file under the 'image' field.
    """
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"File not found: {image_path}")

    with open(image_path, "rb") as f:
        files = {"image": (os.path.basename(image_path), f, "image/jpeg")}
        try:
            resp = requests.post(api_url, files=files, timeout=30)
        except requests.RequestException as e:
            raise RuntimeError(f"HTTP request error: {e}")

    if resp.status_code != 200:
        raise RuntimeError(f"API returned status {resp.status_code}: {resp.text}")

    try:
        data = resp.json()
    except json.JSONDecodeError:
        raise RuntimeError(f"API response is not valid JSON: {resp.text}")

    return data

def main():
    if len(sys.argv) < 2:
        print("Usage: python inference.py image.jpg")
        sys.exit(1)

    image_path = sys.argv[1]
    output_path = "output.jpg"

    # Send the image to the API
    print(f"Sending image '{image_path}' to API ({API_URL})...")
    try:
        result = send_image_for_inference(image_path, API_URL)
    except Exception as e:
        print("Error:", e)
        sys.exit(1)

    # Print the JSON response
    print("JSON response from API:")
    print(json.dumps(result, indent=2, ensure_ascii=False))

    # Expecting format: { "boxes": [[x1,y1,x2,y2], ...], "scores": [0.95, ...] }
    boxes = result.get("boxes", [])
    if not isinstance(boxes, list):
        print("Warning: 'boxes' is not a list. Nothing to draw.")
        boxes = []

    # Draw boxes and save output image
    try:
        draw_boxes(image_path, boxes, output_path)
        print(f"Result image saved to '{output_path}'.")
    except Exception as e:
        print("Error drawing boxes:", e)
        sys.exit(1)

if __name__ == "__main__":
    main()
