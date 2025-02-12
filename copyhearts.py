from PIL import Image
import os

# Input and output directory paths
input_dir = "Copyhearts"  # Change this to your image folder
output_dir = "Copydest"

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

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
                    pixels[x, y] = (255, 255, 255, 255)  # Set to pure white

        # Save the modified image
        img.save(output_path)
        print(f"Processed: {filename}")
    else:
        print(f"Skipping {filename}, file not found.")

print("Processing complete. Images saved in:", output_dir)


print("Processing complete. Images saved in:", output_dir)