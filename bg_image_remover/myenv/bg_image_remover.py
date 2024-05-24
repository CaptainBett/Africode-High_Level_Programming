from rembg import remove
from PIL import Image
# Open the image file
img_path = r'captain@captain-HP-15-Notebook-PC:~/Pictures/A380.jpeg'
img = Image.open(img_path)
# Remove the background from the image
r = remove(img)
# Save the resulting image with the background removed
output_path = r'captain@captain-HP-15-Notebook-PC:~/Downloads/A380.png'
r.save(output_path)