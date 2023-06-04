import earrings.male as male
import earrings.female as female

import utils.choose_attribute as choose_attribute

earrings = {
    "Male": {
        "None": None,
        "Earring": male,
    },
    "Female": {
        "None": None,
        "Earring": female,
    }
}

earrings_ratio = {
    "Male": {
        "None": 0.5,
        "Earring": 0.5,
    },
    "Female": {
        "None": 0.5,
        "Earring": 0.5,
    }
}


def draw_earrings(draw, head):
    chosen_earring = choose_attribute.main(earrings[head], earrings_ratio[head])

    if earrings[head][chosen_earring] is not None:
        earrings[head][chosen_earring].draw(draw)

    return chosen_earring
