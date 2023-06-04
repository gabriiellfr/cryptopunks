import utils.choose_attribute as choose_attribute

males = {
    "Rounded": [
        (8, 5), (9, 5), (10, 5), (11, 5), (12,  5), (13, 5), (14, 5),  # begin head
        (7, 6), (15, 6),  # begin head
        (6, 7), (16, 7),  # face
        (6, 8), (16, 8),  # face
        (6, 9), (16, 9),  # face
        (6, 10), (16, 10),  # face
        (6, 11), (16, 11),  # face
        (5, 12), (16, 12),  # ear
        (5, 13), (16, 13),  # ear
        (5, 14), (6, 14), (16, 14),  # ear
        (6, 15), (16, 15),  # face
        (6, 16), (16, 16),  # face
        (6, 17), (16, 17),  # face
        (6, 18), (16, 18),  # face
        (6, 19), (16, 19),  # begin face
        (6, 20), (15, 20),  # chin
        (6, 21), (10, 21), (14, 21),  # chin
        (6, 22), (10, 22), (11, 22), (12, 22), (13, 22),  # neck
        (6, 23), (10, 23),  # neck
    ],
    "Square": [
        (8, 5), (9, 5), (10, 5), (11, 5), (12, 5), (13, 5), (14, 5),  # begin head
        (7, 6), (15, 6),  # begin head
        (6, 7), (16, 7),  # face
        (6, 8), (16, 8),  # face
        (6, 9), (16, 9),  # face
        (6, 10), (16, 10),  # face
        (6, 11), (16, 11),  # face
        (5, 12), (16, 12),  # ear
        (5, 13), (16, 13),  # ear
        (5, 14), (6, 14), (16, 14),  # ear
        (6, 15), (16, 15),  # face
        (6, 16), (16, 16),  # face
        (6, 17), (16, 17),  # face
        (6, 18), (16, 18),  # face
        (6, 19), (16, 19),  # begin face
        (6, 20), (15, 20),  # chin
        (6, 21), (10, 21), (11, 21), (12, 21), (13, 21), (14, 21),  # chin
        (6, 22), (10, 22),  # neck
        (6, 23), (10, 23),  # neck
    ]
}

males_ratio = {
    "Square": 0.3,
    "Rounded": 0.5,
}

def draw(draw):
    head_choice = choose_attribute.main(males, males_ratio)

    draw.point(males[head_choice], fill=(0, 0, 0))

    return head_choice, males[head_choice]
