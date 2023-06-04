from PIL import Image, ImageDraw
import random

BACKGROUND_COLORS = [(80,106,119), (120,67,63), (87,61,119)]

def create():
    bg_color = random.choice(BACKGROUND_COLORS)
    image = Image.new('RGB', (24, 24), bg_color)
    draw = ImageDraw.Draw(image)

    return image, draw, bg_color