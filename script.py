import os
import cv2
import numpy as np
from PIL import Image, ImageEnhance

input_folder = "**FolderPath**"  # Folder containing original images
output_light_folder = "**FolderPath**"
output_dark_folder = "**FolderPath**"

# Create output directories if not exist
os.makedirs(output_light_folder, exist_ok=True)
os.makedirs(output_dark_folder, exist_ok=True)

def adjust_brightness_contrast(image, brightness=0, contrast=0):
    """
    Adjust brightness and contrast of an image using OpenCV.
    Brightness range: -100 to 100
    Contrast range: -100 to 100
    """
    img = np.int16(image)
    img = img * (contrast / 127 + 1) - contrast + brightness
    img = np.clip(img, 0, 255)
    return np.uint8(img)

def enhance_image(image_path, output_light, output_dark):
    """ Process image to create light and dark variants """
    img = cv2.imread(image_path)
    
    # Light variant
    light_img = adjust_brightness_contrast(img, brightness=30, contrast=20)  # Adjust values as needed
    cv2.imwrite(output_light, light_img)

    # Dark variant
    dark_img = adjust_brightness_contrast(img, brightness=-30, contrast=-20)  # Adjust values as needed
    cv2.imwrite(output_dark, dark_img)

def process_images():
    """ Loop through all images and generate variants """
    for filename in os.listdir(input_folder):
        if filename.endswith(('.JPG', '.png', '.jpeg')):  
            input_path = os.path.join(input_folder, filename)
            output_light = os.path.join(output_light_folder, filename)
            output_dark = os.path.join(output_dark_folder, filename)
            
            enhance_image(input_path, output_light, output_dark)
            print(f"Processed: {filename}")

process_images()
print("✅ Image processing complete. Check output_images folder.")
