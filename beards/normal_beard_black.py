normal_black_beard_pixels_A = [
    (7, 15),
    (7, 16), (8, 16), (15, 16),

    (7, 17), (8, 17), (9, 17), (10, 17), (11, 17),
    (12, 17), (13, 17), (14, 17), (15, 17),

    (7, 18), (8, 18), (9, 18), (10, 18), (14, 18), (15, 18),

    (8, 19), (9, 19), (10, 19), (11, 19),
    (12, 19), (13, 19), (14, 19), (15, 19),

    (9, 20), (10, 20), (11, 20),
    (12, 20), (13, 20), (14, 20), (15, 20),
]

normal_black_beard_pixels_B = [
    (11, 18), (12, 18), (13, 18),
]


def draw(draw):
    draw.point(normal_black_beard_pixels_A, fill=(0, 0, 0))
    draw.point(normal_black_beard_pixels_B, fill=(134, 88, 30))
