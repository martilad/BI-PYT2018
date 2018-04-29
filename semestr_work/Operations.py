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
        self.resize_img(1.5, 'x')
        #self.resize_img(1.1, 'x')

    def get_view(self):
        #return self.image_origin
        return Image.fromarray(self.view, 'RGB')

    def resize_img(self, percent, axis):
        if axis == 'x':
            if percent < 1:
                to_del = random.sample(range(0, len(self.view)), int(len(self.view)*percent))
                to_del.sort(key=int)
                image = np.zeros((len(to_del), len(self.view[0]), 3), dtype=np.uint8)
                x = 0
                for i in to_del:
                    image[x] = self.view[i]
                    x += 1
            elif percent > 1:
                new_lines = int(len(self.view)*percent) - len(self.view)
                print(new_lines)
                to_add = random.sample(range(0, len(self.view)), new_lines) 
                to_add.sort(key=int)
                image = np.zeros((len(self.view) + new_lines, len(self.view[0]), 3), dtype=np.uint8)
                x = 0
                n = 0
                for i in range(len(image)):
                    if x in to_add:
                        image[i] = self.view[n]
                    else:
                        image[i] = self.view[n]
                        n += 1
                    x += 1

        elif axis == 'y':
            if percent < 100:
                to_del = random.sample(range(0, len(self.view[0])), int(len(self.view[0])*percent))
                to_del.sort(key=int)
                image = np.zeros((len(self.view), len(to_del), 3), dtype=np.uint8)
                y = 0
                for i in to_del:
                    image[:,y] = self.view[:,i]
                    y += 1

            elif percent > 100:
                """"""
       
        self.view = image


