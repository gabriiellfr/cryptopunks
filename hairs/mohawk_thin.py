hair_pixels_A = {
    "Male": [
        (11, 1),
        (10, 2), (12, 2),
        (10, 3), (12, 3),
        (10, 4), (12, 4),
        (10, 5), (12, 5),
        (10, 6), (12, 6),
    ],
    "Female": [
        (12, 3),
        (11, 4), (13, 4),
        (11, 5), (13, 5),
        (11, 6), (13, 6),
        (11, 7), (13, 7),
        (11, 8), (13, 8),
    ]
}

hair_pixels_B = {
    "Male": [
        (11, 2),
        (11, 3),
        (11, 4),
        (11, 5),
        (11, 6),
    ],
    "Female": [
        (12, 4),
        (12, 5),
        (12, 6),
        (12, 7),
        (12, 8),
    ]
}

hair_color = [
    (0, 0, 0),
    (85, 85, 85)
]


def draw(draw, head):
    draw.point(hair_pixels_A[head], fill=hair_color[0])
    draw.point(hair_pixels_B[head], fill=hair_color[1])
