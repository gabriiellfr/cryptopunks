import random

EYE_COLORS = [(0, 0, 0)]

eye_pixels = {
    "Male": [(9, 12), (14, 12)],
    "Female": [(9, 13), (14, 13)],
}

def draw(draw, head):
    eye_color = random.choice(EYE_COLORS)

    for pixel in eye_pixels[head]:
        draw.point(pixel, fill=eye_color)