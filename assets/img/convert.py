import os
import subprocess
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
        # Handle PNG files (Interlaced using ImageMagick v6)
        if ext.endswith(".png"):
            # v6 uses 'convert' directly instead of 'magick convert'
            cmd = ["convert", filename, "-interlace", "PNG", output_path]
            subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"Interlaced PNG: {filename}")
            
        # Handle JPEG files (Progressive using Pillow)
        elif ext.endswith((".jpg", ".jpeg")):
            with Image.open(filename) as img:
                img.save(output_path, "JPEG", progressive=True, optimize=True)
            print(f"Progressive JPEG: {filename}")
            
    except subprocess.CalledProcessError:
        print(f"Error processing PNG with ImageMagick v6: {filename}")
    except Exception as e:
        print(f"Error processing {filename}: {e}")
