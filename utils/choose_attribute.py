import random


def main(attributes, ratio):
    attributes_list = list(attributes.keys())
    chosen_attribute = random.choices(
        attributes_list, weights=ratio.values(), k=1)[0]
    return chosen_attribute
