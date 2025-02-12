from PIL import Image
import os

# Input and output directory paths
base_dir = "project/public/Animations/Animals"  # Change this to your image folder
output_dir = "Copydest"

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)


for subdir in os.listdir(base_dir):
    subdir_path = os.path.join(base_dir, subdir)

    # List all items inside each subdirectory
    if os.path.isdir(subdir_path):
        for item in os.listdir(subdir_path):
            item_path = os.path.join(subdir_path, item)
            if item[0] == ".":
                continue
            for photo in os.listdir(item_path):
                photo_path = os.path.join(item_path, photo)
                filename = f"{photo}r.png"  # File name format

                input_path = photo_path
                output_path = inputtileStack.shift()_path

                if os.path.exists(input_path):
                    img = Image.open(input_path).convert("RGBA")  # Ensure image has an alpha channel
                    pixels = img.load()  # Access pixel data

                    for y in range(img.height):
                        for x in range(img.width):
                            r, g, b, a = pixels[x, y]  # Get RGBA values

                            # If the pixel is non-empty (not fully transparent and not already white)
                            if a > 0 and (r, g, b) != (255, 255, 255):  
                                pixels[x, y] = (128, 0, 0, 255)  # Set to pure white

                    # Save the modified image
                    img.save(output_path)
exit()

# Process each image in the input directory
for i in range(1,21):
    filename = f"{i}.png"  # File name format
    input_path = os.path.join(input_dir, filename)
    output_path = os.path.join(output_dir, filename)

    if os.path.exists(input_path):  # Ensure file exists
        img = Image.open(input_path).convert("RGBA")  # Ensure image has an alpha channel
        pixels = img.load()  # Access pixel data

        for y in range(img.height):
            for x in range(img.width):
                r, g, b, a = pixels[x, y]  # Get RGBA values

                # If the pixel is non-empty (not fully transparent and not already white)
                if a > 0 and (r, g, b) != (255, 255, 255):  
                    pixels[x, y] = (128, 0, 0, 255)  # Set to pure white

        # Save the modified image
        img.save(output_path)
        print(f"Processed: {filename}")
    else:
        print(f"Skipping {filename}, file not found.")

print("Processing complete. Images saved in:", output_dir)


print("Processing complete. Images saved in:", output_dir)