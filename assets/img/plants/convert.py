import os
from PIL import Image

# Create an output directory
output_dir = "progressive_output"
os.makedirs(output_dir, exist_ok=True)

# Process files in the current directory
for filename in os.listdir("."):
    ext = filename.lower()
    
    # Skip the script itself and any directories
    if filename == "convert.py" or os.path.isdir(filename):
        continue
        
    output_path = os.path.join(output_dir, filename)
    
    try:
        # Handle PNG files (Interlaced)
        if ext.endswith(".png"):
            with Image.open(filename) as img:
                img.save(output_path, "PNG", optimize=True)
                print(f"Interlaced PNG: {filename}")
                
        # Handle JPEG files (Progressive)
        elif ext.endswith((".jpg", ".jpeg")):
            with Image.open(filename) as img:
                img.save(output_path, "JPEG", progressive=True, optimize=True)
                print(f"Progressive JPEG: {filename}")
                
    except Exception as e:
        print(f"Error processing {filename}: {e}")
