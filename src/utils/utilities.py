from PIL import Image
import os
import requests
from io import BytesIO

current_dir = os.getcwd()
os.chdir(current_dir + "/../")


def dir_check(dir_location):
    isExist = os.path.exists(dir_location)
    if not isExist:
        # Create a new directory because it does not exist
        os.makedirs(dir_location)
        print("The new directory is created!")
    else:
        print("directory already exists!")



def load_image(img_url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"  # Pretend to be a browser
        }
        response = requests.get(img_url, headers=headers, timeout=10)
        if response.status_code != 200:
            print(f"Failed to fetch image. Status code: {response.status_code}")
            return None

        img = Image.open(BytesIO(response.content)).convert("RGB")
        return img
    except Exception as e:
        print(f"Exception occurred while loading image: {e}")
        return None
