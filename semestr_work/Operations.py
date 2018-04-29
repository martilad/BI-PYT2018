from PIL import Image
import numpy as np
import random
class Operations:
    def __init__(self):
        self.load = False

    def load_image(self, path):
        self.path = path
        self.image_origin = Image.open(path)
        self.image = np.asarray(self.image_origin)
        self.view = np.asarray(self.image_origin)
        self.resize_img(2.0, 'x')
        self.resize_img(2.0, 'y')

    def get_view(self):
        #return self.image_origin
        return Image.fromarray(self.view, 'RGB')

    def resize_img(self, percent, axis):
        if axis == 'x':
            if percent < 1:
                self.downsize_x(percent)
            elif percent > 1:
                self.upsize_x(percent)
        elif axis == 'y':
            if percent < 1:
                self.downsize_y(percent)
            elif percent > 1:
                self.upsize_y(percent)

    def downsize_x(self, percent):
        to_sur = random.sample(range(0, len(self.view)), int(len(self.view)*percent))
        to_sur.sort(key=int)
        image = np.zeros((len(to_sur), len(self.view[0]), 3), dtype=np.uint8)
        x = 0
        for i in to_sur:
            image[x] = self.view[i]
            x += 1
        self.view = image

    def downsize_y(self, percent):
        to_sur = random.sample(range(0, len(self.view[0])), int(len(self.view[0])*percent))
        to_sur.sort(key=int)
        image = np.zeros((len(self.view), len(to_sur), 3), dtype=np.uint8)
        y = 0
        for i in to_sur:
            image[:,y] = self.view[:,i]
            y += 1
        self.view = image

    def upsize_x(self, percent):
        new_lines = int(len(self.view)*percent) - len(self.view)
        to_add = random.sample(range(0, len(self.view)), new_lines) 
        to_add.sort(key=int)
        image = np.zeros((len(self.view) + new_lines, len(self.view[0]), 3), dtype=np.uint8)
        n = 0
        i = 0
        while True:
            if n == len(self.view):
                break
            if n in to_add:
                image[i] = self.view[n]
                i += 1
            image[i] = self.view[n]
            n += 1
            i += 1
        self.view = image

    def upsize_y(self, percent):
        new_lines = int(len(self.view[0])*percent) - len(self.view[0])
        to_add = random.sample(range(0, len(self.view[0])), new_lines) 
        to_add.sort(key=int)
        image = np.zeros((len(self.view), len(self.view[0]) + new_lines, 3), dtype=np.uint8)
        n = 0
        i = 0
        while True:
            if n == len(self.view[0]):
                break
            if n in to_add:
                image[:,i] = self.view[:,n]
                i += 1
            image[:,i] = self.view[:,n]
            n += 1
            i += 1
        self.view = image




