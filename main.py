from PIL import Image

import grid.main as grid
import heads.main as heads

num_images = 1

for i in range(num_images):
    image, draw, bg_color = grid.create()

    head, head_type, head_outline_pixels = heads.draw_head(draw)

    image = image.resize((400, 400), Image.NEAREST)
    image_file_name = f"./punks/cryptopunk_{i}.png"
    image.save(image_file_name)
