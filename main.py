from PIL import Image

import grid.main as grid

image, draw, bg_color = grid.create()

image = image.resize((400, 400), Image.NEAREST)
image_file_name = f"./punks/cryptopunk.png"
image.save(image_file_name)