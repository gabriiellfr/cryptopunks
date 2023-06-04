cigarette_pixels_A = [
    (14, 17), (15, 17), (16, 17), 
    (17, 17), (18, 17), (19, 17),

    (13, 18), (20, 18),

    (14, 19), (15, 19), (16, 19), 
    (17, 19), (18, 19), (19, 19),
]

cigarette_pixels_B = [
    (14, 18), (15, 18), (16, 18), 
    (17, 18), (18, 18)
]

cigarette_pixels_C = [
    (19, 18)
]

cigarette_pixels_D = [
    (19, 10), (19, 11), (19, 12), (19, 13), 
    (19, 14), (19, 15)
]

def draw(draw, head):
    draw.point(cigarette_pixels_A, fill=(0, 0, 0))
    draw.point(cigarette_pixels_B, fill=(198,198,198))
    draw.point(cigarette_pixels_C, fill=(226,92,37))
    draw.point(cigarette_pixels_D, fill=(151,163,171))
