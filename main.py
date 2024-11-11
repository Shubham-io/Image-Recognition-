from PIL import Image
import numpy as np

def process_image(image_path):
    # Load the image
    img = Image.open(image_path).convert("RGB")
    img_array = np.array(img)

    
    # Get the dimensions of the image
    height, width, _ = img_array.shape
 
    
    # Create empty arrays for red, green, and blue channels
    red_array = np.zeros((height, width, 3), dtype=np.uint8)
    green_array = np.zeros((height, width, 3), dtype=np.uint8)
    blue_array = np.zeros((height, width, 3), dtype=np.uint8)
 
    
    # Process each pixel and set only the respective color component in each array
    for i in range(height):
        for j in range(width):
            r, g, b = img_array[i, j]
            if r > g and r > b:
     
                red_array[i, j] = [r, 0, 0]
            elif g > r and g > b:

                green_array[i, j] = [0, g, 0]
            elif b > r and b > g:

                blue_array[i, j] = [0, 0, b]

    return red_array, green_array, blue_array

# Example usage
image_path = './img/sample1.jpg'
red_array, green_array, blue_array = process_image(image_path)

# Converting the arrays back to images to visualize the separated colors
red_image = Image.fromarray(red_array)
green_image = Image.fromarray(green_array)
blue_image = Image.fromarray(blue_array)

# Display the images
red_image.show(title="Red Pixels Only")
green_image.show(title="Green Pixels Only")
blue_image.show(title="Blue Pixels Only")
