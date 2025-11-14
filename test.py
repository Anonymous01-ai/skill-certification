from PIL import Image
import io
import cairosvg
import subprocess

# Convert PNG to SVG using potrace via Pillow and ImageMagick
# Step 1: Convert image to black & white PNM format
image = Image.open("SkillCertLogo.png").convert("L")
image.save("temp.pnm")

# Step 2: Use potrace to vectorize it (you may need to install potrace first)
subprocess.run(["potrace", "temp.pnm", "--svg", "-o", "SkillCertLogo.svg"])

print("✅ SVG file created: SkillCertLogo.svg")
