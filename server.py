from flask import Flask, request, jsonify

import cv2
import numpy as np

import torch
from ultralytics import YOLO

import time

# flask init
app = Flask(__name__)

# model init and warmup
device  = 'cuda' if torch.cuda.is_available() else 'cpu'
model = YOLO('./ckpts/yolov10m.pt').to(device)

dummy_input = np.zeros((640, 640, 3), dtype=np.uint8)
_ = model(dummy_input)

@app.route('/predict', methods=['POST'])
def predict():
    # TODO: incorrect key error / no image error

    file = request.files['file']
    try:
        bin_img = file.read()
        image_arr = np.frombuffer(bin_img, np.uint8)
        image = cv2.imdecode(image_arr, cv2.IMREAD_COLOR)  # BGR
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        start_time = time.time()
        results = model(image)
        end_time = time.time()

        predictions = []
        for box in results[0].boxes:
            cls_id = int(box.cls)
            conf = float(box.conf)
            bbox = [float(x) for x in box.xyxy[0].tolist()]
            predictions.append({
                "class_id": cls_id,
                "confidence": round(conf, 4),
                "bbox": bbox
            })

        return jsonify({
            "success": True,
            "inference_time": round(end_time - start_time, 4),
            "predictions": predictions
        })

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
