import tkinter as tk

# Create a Tkinter application window
window = tk.Tk()

# Create a 24x24 grid to store the pixel values
grid = [[0] * 24 for _ in range(24)]

# Create a list to store the pixel positions
head_pixels = [

]

def handle_click(event):
    # Calculate the cell index based on the click position
    x = event.x // 10
    y = event.y // 10

    # Toggle the grid cell value
    grid[y][x] = 1 - grid[y][x]  # Toggle between 0 and 1

    # Update the cell color based on the value
    cell_color = "black" if grid[y][x] == 1 else "white"
    canvas.itemconfig(cells[y][x], fill=cell_color)

    # If cell is black (meaning grid[y][x] == 1), append to head_pixels and display the pixel
    if grid[y][x] == 1:
        head_pixels.append((x, y))
        head_pixels_text.insert(tk.END, f"({x}, {y})\n")  # Add the pixel to the text widget
    else:
        # If cell is turned off, remove it from head_pixels and refresh the text widget
        head_pixels.remove((x, y))
        head_pixels_text.delete("1.0", tk.END)
        for pixel in head_pixels:
            x, y = pixel
            head_pixels_text.insert(tk.END, f"({x}, {y})\n")


# Function to update the head_pixels array
def update_head_pixels():
    # Clear the head_pixels list
    head_pixels.clear()

    # Iterate over the grid to generate the pixel positions
    for y in range(24):
        for x in range(24):
            if grid[y][x] == 1:
                head_pixels.append((x, y))

    # Show the updated head_pixels array in real-time
    head_pixels_text.delete("1.0", tk.END)
    for pixel in head_pixels:
        x, y = pixel
        head_pixels_text.insert(tk.END, f"({x}, {y})\n")

# Function to clear the grid and head_pixels array
def clear_grid():
    # Clear the grid values
    for y in range(24):
        for x in range(24):
            grid[y][x] = 0
            canvas.itemconfig(cells[y][x], fill="white")

    # Clear the head_pixels text widget
    head_pixels_text.delete("1.0", tk.END)

    for pixel in head_pixels:
        x, y = pixel
        grid[y][x] = 1
        canvas.itemconfig(cells[y][x], fill="black")

# Create a canvas to display the grid
canvas = tk.Canvas(window, width=240, height=240, bg="white")
canvas.pack()

# Create a nested list to store the references to the canvas rectangles
cells = [[None] * 24 for _ in range(24)]

# Create the grid cells on the canvas
for y in range(24):
    for x in range(24):
        rect = canvas.create_rectangle(x * 10, y * 10, (x + 1) * 10, (y + 1) * 10, fill="white")
        cells[y][x] = rect

# Set the default pixels on the grid
for pixel in head_pixels:
    x, y = pixel
    grid[y][x] = 1
    canvas.itemconfig(cells[y][x], fill="black")

# Create a text widget to display the head_pixels array
head_pixels_text = tk.Text(window, width=10, height=15)
head_pixels_text.pack()

# Create a "Clear" button
clear_button = tk.Button(window, text="Clear", command=clear_grid)
clear_button.pack()

# Bind the mouse click event to the canvas
canvas.bind("<Button-1>", handle_click)

# Run the Tkinter event loop
window.mainloop()
