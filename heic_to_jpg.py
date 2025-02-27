import os
from pillow_heif import register_heif_opener
from PIL import Image

# Register HEIC format support
register_heif_opener()

def convert_heic_to_jpg(input_folder, output_folder):
    """Convert all .heic images in input_folder to .jpg and save to output_folder."""
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)  # Create the output directory if it doesn't exist

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".heic"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename.replace(".HEIC", ".jpg"))

            try:
                image = Image.open(input_path)
                image.convert("RGB").save(output_path, "JPEG")
                print(f"Converted: {input_path} -> {output_path}")
            except Exception as e:
                print(f"Failed to convert {input_path}: {e}")

# Example usage
input_folder = "**FolderPath**"
output_folder = "**FolderPath**"

convert_heic_to_jpg(input_folder, output_folder)
