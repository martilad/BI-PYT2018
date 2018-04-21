import numpy as np
from PIL import Image

# mandelbrot set settings
height_of_image = 20000
width_of_image = 20000
iteration = 30
min_real = -2.1
max_real = 0.8
min_imag = -1.5
max_imag = 1.4
scale_on_real = (max_real - min_real) / (width_of_image - 1)
scale_on_imag = (max_imag - min_imag) / (height_of_image - 1)

image = np.zeros((height_of_image, width_of_image, 3), dtype=np.uint8)

for y in range(height_of_image):
    if y % 100 == 0:
        print(y)
    for x in range(width_of_image):
        complex_number = complex(min_real + (x * scale_on_real), min_imag + (y * scale_on_imag))
        is_inside = True
        complex_line = complex(0,0)
        for z in range(0, iteration):
            complex_line = (complex_line*complex_line) + complex_number
            if abs(complex_line) > 4:
                is_inside = False
                if (z < int((iteration * (6/10)))):
                    r = z * 1 % 256
                    g = (z * (240/(iteration * (6/10))) + 15) % 256
                    b = z * 1 % 256
                else:
                    r = z * (255/(iteration* (4/10))) % 256
                    g = z * 1 % 256
                    b = z * 1 % 256
                image[y][x] = [r,g,b]
                break

        if is_inside:
            image[y][x] = [0,0,0]

out = Image.fromarray(image, 'RGB')
out.save('image.png')
