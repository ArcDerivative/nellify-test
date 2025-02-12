from PIL import Image
import os

# Input and output directory paths
input_dir = "Copyhearts"  # Change this to your image folder
output_dir = "Copydest"

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Process each image in the input directory
for i in range(1,21):
    

    # Get original dimensions
    width, height = 160, 160

    # Create a new image with extended size
    canvas = Image.new("RGBA", (width, height))

    for j in range(1, i+1):
        filename = str(j) + ".png"
        img_path = os.path.join(input_dir, filename)
        img = Image.open(img_path).convert("RGBA")
        canvas.paste(img,(0,0),img)

    # Paste the original image into the new image
    
    # Save the new image
    canvas.save(os.path.join(output_dir, filename))

print("Processing complete. Images saved in:", output_dir)