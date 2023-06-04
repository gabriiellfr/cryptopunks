import utils.choose_attribute as choose_attribute
import utils.skin_fill as skin_fill

skins = {
    "Dark-skinned": (88, 60, 45), 
    "Mid-skinned": (152, 110, 82), 
    "Light-skinned": (205, 170, 125), 
    "Albino-skinned": (233,217,216),
}

skins_ratio = {
    "Dark-skinned": 0.25, 
    "Mid-skinned": 0.25, 
    "Light-skinned": 0.25, 
    "Albino-skinned": 0.25,
}

def draw_skin(draw, head_outline_pixels):
    skin_pixels = skin_fill.main((10, 10), head_outline_pixels, 24, 24)

    skin_color = choose_attribute.main(skins, skins_ratio)

    draw.point(skin_pixels, fill=skins[skin_color])

    return skin_color
