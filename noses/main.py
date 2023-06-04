# Define the pixel layout of the eye
nose_pixels = {
    "Male": [(12, 15), (13, 15)],
    "Female": [(12, 16)]
}

def draw_nose(draw, head):
    draw.point(nose_pixels[head], fill=(0, 0, 0))