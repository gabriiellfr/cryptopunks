from PIL import Image
import json
import os
import grid.main as grid
import heads.main as heads
import skins.main as skins
import eyes.main as eyes
import noses.main as noses
import mouths.main as mouths
import hairs.main as hairs
import beards.main as beards
import props.main as props

current_dir = os.path.dirname(os.path.abspath(__file__))

# Define the directory name
dir_name = "punks"
output_dir = os.path.join(current_dir, dir_name)

# Ensure the directory exists
os.makedirs(output_dir, exist_ok=True)

# Number of NFTs to generate
num_images = 1

for i in range(num_images):
    image, draw, bg_color = grid.create()

    head, head_type, head_outline_pixels = heads.draw_head(draw)
    skin = skins.draw_skin(draw, head_outline_pixels)
    nose = noses.draw_nose(draw, head)
    mouth = mouths.draw_mouth(draw, head)
    hair = hairs.draw_hair(draw, head)
    eyes_d = eyes.draw_eyes(draw, head)
    beard = beards.draw_beard(draw, head, head_type)
    prop = props.draw_props(draw, head)

    print(f"head: {head}, head_type: {head_type}, skin: {skin}, eyes: {eyes_d}, \nmouth: {mouth}, hair: {hair}, prop: {prop}, beard: {beard}")

    # Save each image with a unique name
    image = image.resize((400, 400), Image.NEAREST)
    image_file_name = f"./punks/cryptopunk_{i}.png"
    image.save(image_file_name)

    # Define metadata for this NFT
    metadata = {
        "name": f"CryptoPunk #{i}",
        "description": "A randomly generated CryptoPunk",
        "image": image_file_name,
        "attributes": [
            {
                "type": "Head",
                "value": head
            },
            {
                "type": "Head Type",
                "value": head_type
            },
            {
                "type": "Skin Color",
                "value": skin
            },
            {
                "type": "Eyes",
                "value": eyes_d
            },
            {
                "type": "Mouth",
                "value": mouth
            },
            {
                "type": "Hair",
                "value": hair
            },
            {
                "type": "Beard",
                "value": beard
            },
            {
                "type": "Prop",
                "value": prop
            }
        ]
    }

    # Save metadata to a JSON file
    with open(f'./punks/cryptopunk_{i}_metadata.json', 'w') as f:
        json.dump(metadata, f)
