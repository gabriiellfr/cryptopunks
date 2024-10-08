glasses_pixels = {
    "Male": [
        (8, 10), (9, 10), (10, 10), (11, 10),
        (13, 10), (14, 10), (15, 10),

        (7, 11), (8, 11), (11, 11), (13, 11), (12, 11),

        (8, 12), (11, 12), (13, 12),

        (8, 13), (9, 13), (10, 13), (11, 13),
        (13, 13), (14, 13), (15, 13),
    ],
    "Female": [
        (8, 11), (9, 11), (10, 11), (11, 11),
        (7, 12), (8, 12), (11, 12),
        (8, 13), (11, 13),
        (9, 14), (10, 14),

        (12, 12),

        (13, 11), (14, 11), (15, 11), (16, 11),
        (13, 12), (16, 12),
        (13, 13), (16, 13),
        (14, 14), (15, 14),
    ]
}

lens_pixels = {
    "Male": [
        (9, 11), (10, 11), (9, 12), (10, 12),
        (14, 11), (15, 11), (14, 12), (15, 12),
    ],
    "Female": [
        (9, 12), (10, 12), (9, 13), (10, 13),
        (14, 12), (15, 12), (14, 13), (15, 13),
    ]
}


def draw(draw, head):
    for pixel in glasses_pixels[head]:
        draw.point(pixel, fill=(0, 0, 0))

    for pixel in lens_pixels[head]:
        draw.point(pixel, fill=(128, 219, 218))
