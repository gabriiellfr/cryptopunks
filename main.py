from PIL import Image

import grid.main as grid
import heads.main as heads
import skins.main as skins
import noses.main as noses
import mouths.main as mouths
import hairs.main as hairs
import eyes.main as eyes

num_images = 1

for i in range(num_images):
    image, draw, bg_color = grid.create()

    head, head_type, head_outline_pixels = heads.draw_head(draw)
    skin = skins.draw_skin(draw, head_outline_pixels)
    nose = noses.draw_nose(draw, head)
    mouth = mouths.draw_mouth(draw, head)
    hair = hairs.draw_hair(draw, head)
    eyes_d = eyes.draw_eyes(draw, head)

    image = image.resize((400, 400), Image.NEAREST)
    image_file_name = f"./punks/cryptopunk_{i}.png"
    image.save(image_file_name)
