big_beard_pixels_A = [
    (17, 17),
    (5, 18), (17, 18),
    (5, 19), (17, 19),
    (5, 20), (17, 20),
    (6, 21), (7, 21), (17, 21),
    (8, 22), (9, 22), (16, 22),
    (11, 23), (12, 23), (13, 23), (14, 23), (15, 23),
]

big_beard_pixels_B = [
    (9, 16), (10, 16), (11, 16), (12, 16), 
    (13, 16), (14, 16), (15, 16),

    (7, 17), (8, 17), (9, 17), (10, 17), (11, 17), 
    (12, 17), (13, 17), (14, 17), (15, 17), (16, 17),

    (6, 18), (7, 18), (8, 18), (9, 18), (10, 18), 
    (14, 18), (15, 18), (16, 18),

    (6, 19), (7, 19), (8, 19), (9, 19), (10, 19), (11, 19), 
    (12, 19), (13, 19), (14, 19), (15, 19), (16, 19),

    (6, 20), (7, 20), (8, 20), (9, 20), (10, 20), (11, 20), 
    (12, 20), (13, 20), (14, 20), (15, 20), (16, 20),

    (8, 21), (9, 21), (10, 21), (11, 21), (12, 21), 
    (13, 21), (14, 21), (15, 21), (16, 21),

    (11, 22), (12, 22), (13, 22), (14, 22), (15, 22)
]


def draw(draw):
    draw.point(big_beard_pixels_A, fill=(0, 0, 0))
    draw.point(big_beard_pixels_B, fill=(166, 110, 44))
