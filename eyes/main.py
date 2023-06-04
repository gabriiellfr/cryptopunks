import utils.choose_attribute as choose_attribute

import eyes.eyes_raw as eyes_raw
import eyes.eye_brow as eye_brow
import eyes.threed_glasses as threed_glasses
import eyes.nerd_glasses as nerd_glasses

eyes = {
    "Eye-Brow": eye_brow,
    "3D-Glasses": threed_glasses,
    "Nerd-Glasses": nerd_glasses,
}

eyes_ratio = {
    "Eye-Brow": 0.3,
    "3D-Glasses": 0.3,
    "Nerd-Glasses": 0.3,
}

def draw_eyes(draw, head):
    eyes_raw.draw(draw, head)

    chosen_eyes = choose_attribute.main(eyes, eyes_ratio)

    eyes[chosen_eyes].draw(draw, head)

    return chosen_eyes
