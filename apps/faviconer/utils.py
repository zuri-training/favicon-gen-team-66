import json
import hashlib
import os
from io import BytesIO

import requests
from PIL import Image


def generate_favicon_id(source_url, crop_points, size):
    crop_points = json.dumps(crop_points)
    meta_str = f"{source_url}-{crop_points}-{size}"
    return hashlib.md5(meta_str.encode('utf-8')).hexdigest()


class FaviconGenerator:
    def __init__(self, image: Image.Image, crop_points: dict = None, icon_size: int = 16):
        self.image = image
        self.crop_points = crop_points
        self.icon_size = icon_size
        self.cropped_image = None
        self.favicon = None

    def validate_crop_points(self):
        width, height = self.image.size
        if self.crop_points is None:
            return True, ""
        else:
            if self.crop_points["left"] < 0 or self.crop_points["top"] < 0:
                return False, "Left or Top crop points can't be less than zero"
            elif self.crop_points["right"] > width:
                return False, f"Right crop point can't be greater than width: {width}"
            elif self.crop_points["bottom"] > height:
                return False, f"Bottom crop point can't be greater than height: {height}"
            else:
                return True, ""

    def crop(self):
        width, height = self.image.size
        crop_points = self.crop_points
        if self.crop_points is None:
            min_dimension = min(width, height)
            if min_dimension == width:
                split_gap = abs((height - width) // 2)
                crop_points = {
                    "left": 0,
                    "top": split_gap,
                    "right": width,
                    "bottom": height - split_gap
                }
            else:
                split_gap = abs((height - width) // 2)
                crop_points = {
                    "left": split_gap,
                    "top": 0,
                    "right": width - split_gap,
                    "bottom": height
                }
        self.crop_points = crop_points
        self.cropped_image = self.image.crop((crop_points["left"], crop_points["top"],
                                              crop_points["right"], crop_points["bottom"]))
        return self.cropped_image

    def resize(self):
        self.favicon = self.cropped_image.resize((self.icon_size, self.icon_size))
        return self.favicon

    def generate(self):
        is_valid, message = self.validate_crop_points()
        if not is_valid:
            return is_valid, message

        self.crop()
        return self.resize(), ""


class ImageUtil:
    @staticmethod
    def download(url):
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        return img

    @staticmethod
    def upload(image: Image.Image):
        THUMBSNAP_APIKEY = os.getenv("THUMBSNAP_APIKEY")
        buf = BytesIO()
        # TODO: Fix this hardcoding of JPEG
        image.save(buf, format='JPEG')
        url = 'https://thumbsnap.com/api/upload'
        files = {'media': buf.getvalue()}
        response = requests.post(url, files=files, data={"key": THUMBSNAP_APIKEY})
        try:
            metadata = json.loads(response.text)
            if metadata.get("status") != 200:
                return None
            return metadata.get("data").get("media")
        except json.decoder.JSONDecodeError:
            return None
