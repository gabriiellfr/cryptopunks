EYE_COLORS = [(0, 0, 0)]
EYE_BROW_COLORS = [(134, 88, 30), (210, 156, 95)]

eye_brow_pixels_A = {
    "Male": [(9, 11), (10, 11),
             (14, 11), (15, 11)],
    "Female": [
        (9, 12), (10, 12),
        (14, 12), (15, 12),
    ]
}

eye_brow_pixels_B = {
    "Male": [(10, 12), (15, 12)],
    "Female": [
        (10, 13), (15, 13)
    ]
}


def draw(draw, head):
    for pixel in eye_brow_pixels_A[head]:
        draw.point(pixel, fill=EYE_BROW_COLORS[0])

    for pixel in eye_brow_pixels_B[head]:
        draw.point(pixel, fill=EYE_BROW_COLORS[1])
