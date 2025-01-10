from PIL import Image # this image editor was used to edit mainly the queen images in the interacrive board.
def simplify_image(image_path, output_path):
    # Open the image
    img = Image.open(image_path).convert("L")  # Convert to grayscale
    data = img.load()

    # Iterate through each pixel
    for y in range(img.height):
        for x in range(img.width):
            # Get the pixel value
            pixel = data[x, y]

            # Apply thresholds
            if 200 <= pixel <= 255:  # Light-gray to white
                data[x, y] = 0
            else:  # Dark-gray to black
                data[x, y] = 255

    # Save the modified image
    img.save(output_path)
    print(f"Image simplified and saved to {output_path}")


# Example usage
simplify_image("images/new_black_queen.png", "images/new_white_queen.png")