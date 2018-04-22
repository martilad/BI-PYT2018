from tkinter import filedialog
import tkinter as tk
import os 
from Operations import App
from PIL import ImageTk, Image

class GUI:
    def __init__(self, root):
        self.root = root
        self.image = App()
        display_text = tk.StringVar()
        self.label = tk.Label(root, height=4, width=30, font=40, textvariable=display_text)
        self.label.pack()
        display_text.set("Lets start...")

    def image_to_window(self):
        self.label.pack_forget()
        #Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
        img = ImageTk.PhotoImage(self.image.get_view())
        #img = ImageTk.PhotoImage(Image.open("/home/ladislav/develop/BI-PYT/test.png"))

        #The Label widget is a standard Tkinter widget used to display a text or image on the screen.
        panel = tk.Label(self.root, image = img)

        #The Pack geometry manager packs widgets in rows or columns.
        panel.pack(side = "right", fill = "both", expand = "yes")
        #self.root.update()
        self.root.mainloop()

    def load_file(self):
        dir_path = os.getcwd()
        self.root.filename =  tk.filedialog.askopenfilename(initialdir = dir_path,title = "Select file",filetypes = (("pictures","*.jpg *.png *.tiff *.bmp"),("all files","*.*")))
        self.image.load_image(self.root.filename)
        self.image_to_window()

    def about_dialog(self):
        T = tk.Toplevel(self.root)
        display_text = tk.StringVar()
        label = tk.Label(T, height=4, width=30, font=40, textvariable=display_text)
        label.grid(row=4, columnspan=3)
        display_text.set("This app is created\n as semestral work \n in subject BI-PYT (Python)\n on Faculty of Information Technology")

    def not_implement(self):
        print("This function is not implemet...")

    def create_menu_to_root(self, root):
        menu_bar = tk.Menu(root)

        main_menu = tk.Menu(menu_bar, tearoff=0)

        main_menu.add_command(label="Open", command=self.load_file, font=40)
        main_menu.add_command(label="Save", command=self.not_implement, font=40)
        main_menu.add_command(label="Save as...", command=self.not_implement, font=40)
        main_menu.add_separator()
        main_menu.add_command(label="Exit", command=root.quit, font=40)
        menu_bar.add_cascade(label="File", menu=main_menu, font=40)


        editmenu = tk.Menu(menu_bar, tearoff=0)
        editmenu.add_command(label="Undo", command=self.not_implement, font=40)
        editmenu.add_command(label="Reset", command=self.not_implement, font=40)
        editmenu.add_command(label="Re-size", command=self.not_implement, font=40)
        editmenu.add_separator()
        editmenu.add_command(label="Rotate 90°C right", command=self.not_implement, font=40)
        editmenu.add_command(label="Rotate 90°C left", command=self.not_implement, font=40)
        editmenu.add_separator()
        editmenu.add_command(label="MirroringX", command=self.not_implement, font=40)
        editmenu.add_command(label="MirroringY", command=self.not_implement, font=40)
        editmenu.add_command(label="Inverse", command=self.not_implement, font=40)
        editmenu.add_separator()
        editmenu.add_command(label="Greyscale", command=self.not_implement, font=40)
        editmenu.add_command(label="Dark", command=self.not_implement, font=40)
        editmenu.add_command(label="Light", command=self.not_implement, font=40)
        editmenu.add_command(label="Highlight", command=self.not_implement, font=40)
        menu_bar.add_cascade(label="Operation", menu=editmenu, font=40)


        helpmenu = tk.Menu(menu_bar, tearoff=0)
        helpmenu.add_command(label="About...", command=self.about_dialog, font=40)
        menu_bar.add_cascade(label="Help", menu=helpmenu, font=40)
        root.config(menu=menu_bar, background='black')