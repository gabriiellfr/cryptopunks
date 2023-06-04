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
        "Normal": 0,
        "Frown": 0.5,
        "Smile": 0.5,
    },
    "Female": {
        "Normal": 0.5,
    }
}

def draw_mouth(draw, head):
    chosen_mouth = choose_attribute.main(mouths[head], mouths_ratio[head])

    draw.point(mouths[head][chosen_mouth], fill=(0, 0, 0))

    return chosen_mouth