import numpy as np
from PIL import Image
import argparse, os

def check_file_picture_name(value):
    filename, file_extension = os.path.splitext(str(value))
    if file_extension != '.png' and file_extension != '.jpg' and file_extension != '.bmp' and file_extension != '.tiff':
         raise argparse.ArgumentTypeError("Invalid name of picture")
    return value

parser=argparse.ArgumentParser("Encryptor for Viegeners cipher")
parser.add_argument("-s", help='size of results image', default=[500,500], nargs=2, type=int)
parser.add_argument("-i", help='number of iteration in', default=15, type=int)
parser.add_argument("-o", help='output file name', default="mandelbrot.png", type=check_file_picture_name)
args = parser.parse_args()
height_of_image = args.s[1] if args.s[1] > 0 else 500
width_of_image = args.s[0] if args.s[0] > 0 else 500
iteration = args.i if args.i > 0 else 15

min_real = -2.1
max_real = 0.8
min_imag = -1.5
max_imag = 1.4
scale_on_real = (max_real - min_real) / width_of_image
scale_on_imag = (max_imag - min_imag) / height_of_image


image = np.zeros((height_of_image, width_of_image, 3), dtype=np.uint8)

for y in range(height_of_image):
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
out.save(args.o)
