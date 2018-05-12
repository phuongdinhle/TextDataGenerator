import cv2
import math
import random
import os
import numpy as np

from PIL import Image, ImageFont, ImageDraw, ImageFilter

class ComputerTextGenerator(object):
    @classmethod
    def generate(cls, text, font):
        image_font = ImageFont.truetype(font=os.path.join('fonts', font), size=32)
        text_width, text_height = image_font.getsize(text)

        txt_img = Image.new('L', (text_width, text_height), 255)

        txt_draw = ImageDraw.Draw(txt_img)

        txt_draw.text((0, 0), text, fill=random.randint(1, 80), font=image_font)

        return txt_img
