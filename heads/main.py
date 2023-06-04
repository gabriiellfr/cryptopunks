import heads.male as male
import heads.female as female

import utils.choose_attribute as choose_attribute

heads = {
    "Male": male,
    "Female": female,
}

head_ratio = {
    "Male": 0.5,
    "Female": 0.5,
}

def draw_head(draw):
    chosen_head = choose_attribute.main(heads, head_ratio)

    head_type, head_outline_pixels = heads[chosen_head].draw(draw)

    return chosen_head, head_type, head_outline_pixels