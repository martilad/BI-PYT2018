from PIL import Image
import numpy as np
class App:
    def __init__(self):
        self.load = False

    def load_image(self, path):
        self.image_origin = Image.open(path)
        self.image = np.asarray(self.image_origin)
        self.view = np.asarray(self.image_origin)

    def get_view(self):
        return self.image_origin
        return Image.fromarray(self.view, 'RGB')


"""path = "test.png"
size = 500, 500
im_temp = Image.open(path)
im_temp = im_temp.resize(size, Image.ANTIALIAS)
#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(im_temp)

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(root, image = img)

#The Pack geometry manager packs widgets in rows or columns.
panel.pack(side = "right", fill = "both", expand = "yes")"""