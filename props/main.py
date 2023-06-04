import props.cigarette as cigarette

import utils.choose_attribute as choose_attribute

props = {
    "None": None,
    "Cigarette": cigarette,
}

props_ratio = {
    "None": 0.5,
    "Cigarette": 0.5,
}

def draw_props(draw, head):
    chosen_props = choose_attribute.main(props, props_ratio)

    if props[chosen_props] is not None:
        props[chosen_props].draw(draw, head)

    return chosen_props
