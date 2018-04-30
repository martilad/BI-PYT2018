from PIL import Image
import numpy as np
import random
MAX_VERTICAL_SIZE = 900
MAX_HORIZONTAL_SIZE = 1900

class Operations:
    def __init__(self):
        self.load = False
        self.stack = []

    def push(self):
        self.stack.append(np.copy(self.image))
        if len(self.stack) > 50:
            self.stack = self.stack[-50:]

    def pop(self):
        if len(self.stack) > 0:
            self.image = self.stack.pop()
            return True
        return "No stack more levels."

    def load_image(self, path):
        self.path = path
        try:
            self.image_origin = Image.open(path)
        except:
            return "Bad file. No Image."
        self.image = np.asarray(self.image_origin)
        self.stack = []
        return True

    def mirror_y(self):
        self.push()
        self.image = self.image[::-1]
        return True

    def mirror_x(self):
        self.push()
        self.image = self.image[:, ::-1]
        return True

    def invert(self):
        self.push()
        self.image = 255 - self.image
        return True

    def reset(self):
        self.push()
        self.image = np.asarray(self.image_origin)
        return True

    def rotate_right(self):
        self.push()
        self.image = np.rot90(self.image, 3)
        return True

    def rotate_left(self):
        self.push()
        self.image = np.rot90(self.image)
        return True

    def save_image(self, path):
        try:
            out = Image.fromarray(self.image, 'RGB')#specifikace ukladani
            out.save(path)
            return True
        except:
            return "Bad file extension."

    def create_and_size_view_sizing_of_view(self):
        self.view = np.copy(self.image)
        if len(self.view) > MAX_VERTICAL_SIZE:
            percent = MAX_VERTICAL_SIZE/len(self.view)
            self.view = self.resize_img(picture=self.view, percent=percent, axis='y')
            self.view = self.resize_img(picture=self.view, percent=percent, axis='x')
        if len(self.view[0]) > MAX_HORIZONTAL_SIZE:
            percent = MAX_HORIZONTAL_SIZE/len(self.view[0])
            self.view = self.resize_img(picture=self.view, percent=1900/percent, axis='y')
            self.view = self.resize_img(picture=self.view, percent=1900/percent, axis='x')

    def get_view(self):
        self.create_and_size_view_sizing_of_view()
        return Image.fromarray(self.view, 'RGB')

    def resize_img(self, picture, percent, axis):
        if percent < 0:
            return
        if axis == 'y':
            if percent < 1:
                return self.downsize_y(picture=picture, percent=percent)
            elif percent > 1:
                while True:
                    if percent > 2:
                        picture = self.upsize_y(picture=picture, percent=2)
                        percent = percent / 2
                    else:
                        return self.upsize_y(picture=picture, percent=percent)
        elif axis == 'x':
            if percent < 1:
                return self.downsize_x(picture=picture, percent=percent)
            elif percent > 1:
                while True:
                    if percent > 2:
                        picture = self.upsize_x(picture=picture, percent=2)
                        percent = percent / 2
                    else:
                        return self.upsize_x(picture=picture, percent=percent)
                

    def downsize_y(self, picture, percent):
        to_sur = random.sample(range(0, len(picture)), int(len(picture)*percent))
        to_sur.sort(key=int)
        image = np.zeros((len(to_sur), len(picture[0]), 3), dtype=np.uint8)
        x = 0
        for i in to_sur:
            image[x] = picture[i]
            x += 1
        return image

    def downsize_x(self, picture, percent):
        to_sur = random.sample(range(0, len(picture[0])), int(len(picture[0])*percent))
        to_sur.sort(key=int)
        image = np.zeros((len(picture), len(to_sur), 3), dtype=np.uint8)
        y = 0
        for i in to_sur:
            image[:,y] = picture[:,i]
            y += 1
        return image

    def upsize_y(self, picture, percent):
        new_lines = int(len(picture)*percent) - len(picture)
        to_add = random.sample(range(0, len(picture)), new_lines) 
        to_add.sort(key=int)
        image = np.zeros((len(picture) + new_lines, len(picture[0]), 3), dtype=np.uint8)
        n = 0
        i = 0
        while True:
            if n == len(picture):
                break
            if n in to_add:
                image[i] = picture[n]
                i += 1
            image[i] = picture[n]
            n += 1
            i += 1
        return image

    def upsize_x(self, picture, percent):
        new_lines = int(len(picture[0])*percent) - len(picture[0])
        to_add = random.sample(range(0, len(picture[0])), new_lines) 
        to_add.sort(key=int)
        image = np.zeros((len(picture), len(picture[0]) + new_lines, 3), dtype=np.uint8)
        n = 0
        i = 0
        while True:
            if n == len(picture[0]):
                break
            if n in to_add:
                image[:,i] = picture[:,n]
                i += 1
            image[:,i] = picture[:,n]
            n += 1
            i += 1
        return image




