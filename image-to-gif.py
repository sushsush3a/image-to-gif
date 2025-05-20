from PIL import Image
import numpy as np
import imageio.v3 as iio

filenames = ['elgato1.jpg','elgato2.jpg']
images = [ ]

base_image = Image.open(filenames[0])
target_size = base_image.size

for filename in filenames:
	img = Image.open(filename).convert("RGB")
	img = img.resize(target_size)
	images.append(np.array(img))              

# Write to GIF
iio.imwrite('elgato.gif', images, duration=500, loop=0)
