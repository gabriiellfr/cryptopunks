import random
import eyes.eye_brow as eye_brow

EYE_COLORS = [(0, 0, 0)]
EYE_BROW_COLORS_A = [(134, 88, 30)]
EYE_BROW_COLORS_B = [(210, 156, 95)]

# Define the pixel layout of the eye
eye_pixels = {
    "Male": [(9, 12), (14, 12)],
    "Female": [(9, 13), (14, 13)],
}

eye_shadow_pixels = [
    (8, 11), (9, 11), (10, 11),  # left eye shadow
    (8, 12), (10, 12),  # left eye shadow
    (8, 13), (9, 13), (10, 13),  # left eye shadow

    (13, 11), (14, 11), (15, 11),  # right eye shadow
    (13, 12), (15, 12),  # right eye shadow
    (13, 13), (14, 13), (15, 13),  # right eye shadow
]


def draw_eyes(draw, head):
    eye_color = random.choice(EYE_COLORS)

    for pixel in eye_pixels[head]:
        draw.point(pixel, fill=eye_color)

    eye_brow.draw(draw, head)

def draw_eye_shadow(draw):
    eye_shadow = (255, 255, 255)

    for pixel in eye_shadow_pixels:
        draw.point(pixel, fill=eye_shadow)

eye_clow_pixels = [
    (9, 11),  # left eye shadow
    (9, 12), (10, 12),  # left eye shadow
    (10, 13),  # left eye shadow
    (9, 14),  # left eye shadow

    (14, 11),  # left eye shadow
    (14, 12), (15, 12),  # left eye shadow
    (15, 13),  # left eye shadow
    (14, 14),  # left eye shadow
]

def draw_eye_clow(draw):
    eye_shadows = [
        (39,89,177),
        (44,81,148),
        (41,62,100)
    ]

    for pixel in eye_clow_pixels:
        draw.point(pixel, fill=random.choice(eye_shadows))