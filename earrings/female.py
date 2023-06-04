earring_pixels = [
    (5, 14), (6, 15)
]
    
earring_stone_pixel = [
    (6, 14)
]

def draw(draw):
    draw.point(earring_pixels, fill=(0, 0, 0,))
    draw.point(earring_stone_pixel, fill=(255,217,37))