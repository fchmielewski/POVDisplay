import numpy as np
import cv2
from PIL import Image

def remap_pixels_color(source_image, target_shape):
    # Get the center of the source image
    center_x, center_y = source_image.shape[1] // 2, source_image.shape[0] // 2

    # Create a polar grid
    theta, radius = np.meshgrid(np.linspace(0, 2*np.pi, target_shape[1]), 
                                np.linspace(0, center_y, target_shape[0]))

    # Convert polar coordinates to Cartesian coordinates
    x = (radius * np.cos(theta) + center_x).astype(int)
    y = (radius * np.sin(theta) + center_y).astype(int)

    # Ensure indices are within bounds
    x = np.clip(x, 0, source_image.shape[1] - 1)
    y = np.clip(y, 0, source_image.shape[0] - 1)

    # Remap pixels for each color channel
    remapped_channels = [source_image[:,:,i][y, x] for i in range(source_image.shape[2])]

    # Stack the remapped channels to get the final remapped image
    remapped_image = np.stack(remapped_channels, axis=-1)

    # Reshape the remapped image to the target shape
    remapped_image = remapped_image.reshape(target_shape[0], target_shape[1], source_image.shape[2])

    return remapped_image

# Load a sample image (replace 'your_image_path.png' with the actual image path)
source_image = cv2.imread('your_image_path.png', cv2.IMREAD_COLOR)

# Set the target shape
target_shape = (36, 226)

# Remap pixels in color
remapped_image_color = remap_pixels_color(source_image, target_shape)

# Save the remapped color image
output_path = 'remapped_image_color.png'
cv2.imwrite(output_path, remapped_image_color)

print(f"Remapped image saved to {output_path}")


# Display the original and remapped images
cv2.imshow('Original Image', source_image)
cv2.imshow('Remapped Image (Color)', remapped_image_color)
cv2.waitKey(0)
cv2.destroyAllWindows()

def convert_image_to_array(image_path):
    # Open the image
    img = Image.open(image_path)

    # Get the size of the image
    width, height = img.size

    # Initialize an empty list to store the Arduino array values
    arduino_array = []

    # Loop through each pixel in the image
    for x in range(width):
        row = []
        for y in range(height):
            # Get the RGB values of the pixel
            r, g, b = img.getpixel((x, y))

            # Convert RGB values to a hexadecimal color code (0xRRGGBB)
            color_code = (r << 16) | (g << 8) | b

            # Append the color code to the row list
            row.append(color_code)

        # Append the row list to the Arduino array
        arduino_array.append(row)

    return arduino_array

def print_arduino_array(arduino_array):
    # Print the Arduino array in a format suitable for Arduino code
    print("{")
    for row in arduino_array:
        print("  {" + ", ".join(f"0x{color:06X}" for color in row) + "},")
    print("};")

if __name__ == "__main__":
    # Replace 'your_image_path.png' with the path to your image file
    image_path = 'your_image_path.png'

    # Convert the image to an Arduino array
    arduino_array = convert_image_to_array(image_path)

    # Print the Arduino array
    print_arduino_array(arduino_array)
