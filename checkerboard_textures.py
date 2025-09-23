from PIL import Image, ImageDraw

# Grid parameters
image_size = 512
cell_size = 16
num_cells = image_size // cell_size

# Colors
light_color = (204, 204, 204)  # #CCCCCC
dark_color = (136, 136, 136)   # #888888

# Create a new image
image = Image.new("RGB", (image_size, image_size), light_color)
draw = ImageDraw.Draw(image)

# Draw checkerboard pattern
for row in range(num_cells):
    for col in range(num_cells):
        if (row + col) % 2 == 0:
            color = light_color
        else:
            color = dark_color
        x0 = col * cell_size
        y0 = row * cell_size
        x1 = x0 + cell_size
        y1 = y0 + cell_size
        draw.rectangle([x0, y0, x1, y1], fill=color)

# Save or show the image
image.save("checkerboard_512x512.png")
image.show()