# Crack Detection — Simple Demo

This small project demonstrates a minimal inference pipeline in Python. It sends an image to an existing inference API (your model hosted elsewhere), receives detected boxes for cracks, and draws red rectangles on the image to show results.

Files included
- `inference.py` : main script. Usage: `python inference.py image.jpg`
- `utils.py` : contains the `draw_boxes` function to draw and save the output image.
- `README.md` : this file.

Requirements
- Python 3
- Install required libraries:
  - requests
  - pillow

Example install:
```
pip install requests pillow
```

How to use
1. Replace the API URL in `inference.py`:
   - Open `inference.py` and change the `API_URL` variable near the top.
   - Example:
     ```
     API_URL = "https://my-server.example/api/predict"
     ```

2. Run inference on an image:
```
python inference.py image.jpg
```
- The script will:
  - send `image.jpg` to the API,
  - print the JSON response to the terminal,
  - draw a red rectangle for each returned box,
  - save the annotated image as `output.jpg`.

Expected API response format
- The script expects a JSON like:
```json
{
  "boxes": [[x1, y1, x2, y2], [x1, y1, x2, y2]],
  "scores": [0.95, 0.87]
}
```
- Only the `boxes` field is used for drawing. Coordinates are pixel values with (0,0) at the top-left.

Notes and limitations
- This is a simple school demo. It does not include advanced error handling, authentication, or retries.
- If your API expects a different file field name than `image`, or a different request format, edit the `send_image_for_inference` function in `inference.py`.

Good luck with your demo!
