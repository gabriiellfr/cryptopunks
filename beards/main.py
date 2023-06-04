import utils.choose_attribute as choose_attribute

import beards.big_beard as big_beard
import beards.normal_beard_black as normal_beard_black

beards = {
    "Male": {
        "Square": {
            "None": None,
            "Big-Beard": big_beard,
            "Normal-Beard-Black": normal_beard_black,
        },
        "Rounded": {
            "None": None,
            "Big-Beard": big_beard,
        }
    },
    "Female": {
        "Normal": {
            "None": None,
        }
    }
}

beards_ratio = {
    "Male": {
        "Square": {
            "None": 0.3,
            "Big-Beard": 0.3,
            "Normal-Beard-Black": 0.3,
        },
        "Rounded": {
            "None": 0.5,
            "Big-Beard": 0.5,
        }
    },
    "Female": {
        "Normal": {
            "None": 1,
        }
    }
}


def draw_beard(draw, head, head_type):
    chosen_beard = choose_attribute.main(
        beards[head][head_type], beards_ratio[head][head_type])

    if beards[head][head_type][chosen_beard] is not None:
        beards[head][head_type][chosen_beard].draw(draw)

    return chosen_beard
