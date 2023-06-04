def main(start, boundary_pixels, width, height):
    x, y = start
    to_fill = []
    checked = set()
    stack = [(x, y)]

    while stack:
        x, y = stack.pop()
        if (x, y) in checked or (x, y) in boundary_pixels or x < 0 or y < 0 or x >= width or y >= height:
            continue
        to_fill.append((x, y))
        checked.add((x, y))
        stack.append((x + 1, y))
        stack.append((x - 1, y))
        stack.append((x, y + 1))
        stack.append((x, y - 1))

    return to_fill