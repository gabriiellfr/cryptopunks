import utils.choose_attribute as choose_attribute
import hairs.wild_white_hair as wild_white_hair
import hairs.mohawk_thin as mohawk_thin

hairs = {
    "Male": {
        "Bald": None,
        "Mohawk-Thin": mohawk_thin,
    },
    "Female": {
        "Bald": None,
        "Wild-White-Hair": wild_white_hair,
        "Mohawk-Thin": mohawk_thin,
    },
}

hairs_ratio = {
    "Male": {
        "Bald": 0.5,
        "Mohawk-Thin": 0.5
    },
    "Female": {
        "Bald": 0.5,
        "Wild-White-Hair": 0.5,
        "Mohawk-Thin": 0.5
    },
}

def draw_hair(draw, head):
    chosen_hair = choose_attribute.main(hairs[head], hairs_ratio[head])

    if hairs[head][chosen_hair] is not None:
        hairs[head][chosen_hair].draw(draw, head)
    
    return chosen_hair