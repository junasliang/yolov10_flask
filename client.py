import requests
import time
import os
from glob import glob
from tqdm import tqdm

API_URL = "http://localhost:8000/predict"
IMAGE_DIR = "test_images"

def send_image(image_path, check=False):
    # read as binary
    with open(image_path, 'rb') as img_file:
        files = {'file': img_file}
        start = time.time()
        response = requests.post(API_URL, files=files)
        elapsed = time.time() - start

    if not check:
        if response.ok:
            print(f"[Done] {os.path.basename(image_path)} | Time: {elapsed:.2f}s | Result:", response.json())
        else:
            print(f"Error on {image_path}:", response.text)

def fps_check(test_img_files):
    print("Running fps calculation...")
    rq_start = time.time()
    for i in tqdm(range(10)):
        for filename in test_img_files:
            if filename.lower().endswith((".jpg", ".jpeg", ".png")):
                send_image(filename, check = True)
    rq_fps = 10*len(test_img_files)//(time.time()-rq_start)
    return rq_fps

if __name__ == "__main__":
    test_img_files = sorted(glob(IMAGE_DIR+"/*"))
    # TODO: fixed iteration, add argparser for better testing
    for filename in test_img_files:
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            send_image(filename)
    print("Inference done!")
    print("\r")
    fps_res = fps_check(test_img_files)
    print(f"FPS: {fps_res}")
