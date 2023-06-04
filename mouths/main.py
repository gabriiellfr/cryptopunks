import utils.choose_attribute as choose_attribute

mouths = {
    "Male": {
        "Normal": [(11, 18), (12, 18), (13, 18)],
        "Frown": [(10, 19), (11, 18), (12, 18), (13, 18)],
        "Smile": [(10, 17), (11, 18), (12, 18), (13, 18)],
    },
    "Female": {
        "Normal": [
            (11, 18), (12, 18), (13, 18)
        ],
    }
}

mouths_ratio = {
    "Male": {
        "Normal": 0.3,
        "Frown": 0.3,
        "Smile": 0.3,
    },
    "Female": {
        "Normal": 1,
    }
}

def draw_mouth(draw, head):
    chosen_mouth = choose_attribute.main(mouths[head], mouths_ratio[head])

    draw.point(mouths[head][chosen_mouth], fill=(0, 0, 0))

    return chosen_mouth