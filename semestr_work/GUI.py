from Operations import Operations
from tkinter import filedialog
from PIL import ImageTk, Image
import tkinter as tk
import os 


class GUI:
    def __init__(self):
        # This creates the main window of an application
        self.root = tk.Tk()
        self.root.title("Semestr work")
        self.create_menu_to_root()
        self.image = Operations()
        display_text = tk.StringVar()
        # This create the main text without picture
        self.label = tk.Label(self.root, height=4, width=30, font=40, textvariable=display_text)
        self.label.pack()
        display_text.set("Lets start...")
        # Create empty picture box
        self.panel = tk.Label(self.root, image = None)
        
        """Start aplications"""
    def start(self):
        # Start the GUI
        self.root.mainloop()

        """Put image view from operation to window"""
    def image_to_window(self):
        # Lost last picture
        self.panel.pack_forget()
        self.panel.destroy()
        # Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
        img = ImageTk.PhotoImage(self.image.get_view())
        # The Label widget is a standard Tkinter widget used to display a text or image on the screen.
        self.panel = tk.Label(self.root, image = img)
        self.panel.img = img
        # The Pack geometry manager packs widgets in rows or columns.
        self.panel.pack()
    
        """Start aplications"""
    def load_file(self):
        dir_path = os.getcwd()
        self.root.filename =  tk.filedialog.askopenfilename(initialdir = dir_path,title = "Select file",filetypes = (("pictures","*.jpg *.png *.tiff *.bmp"),("all files","*.*")))
        self.image.load_image(self.root.filename)
        self.label.pack_forget()
        self.image_to_window()

        """Show about dialog"""
    def about_dialog(self):
        T = tk.Toplevel(self.root)
        display_text = tk.StringVar()
        label = tk.Label(T, height=4, width=30, font=40, textvariable=display_text)
        label.grid(row=4, columnspan=3)
        display_text.set("This app is created\n as semestral work \n in subject BI-PYT (Python)\
            \n on Faculty of Information Technology")

        """Not implement function"""
    def not_implement(self):
        print("This function is not implemet...")


    def action_do(self, number):
        print(number)

        """Init menu bar of aplication"""
    def create_menu_to_root(self):
        menu_bar = tk.Menu(self.root)

        main_menu = tk.Menu(menu_bar, tearoff=0)

        main_menu.add_command(label="Open", command=self.load_file, font=40)
        main_menu.add_command(label="Save", command=self.not_implement, font=40)
        main_menu.add_command(label="Save as...", command=self.not_implement, font=40)
        main_menu.add_separator()
        main_menu.add_command(label="Exit", command=self.root.quit, font=40)
        menu_bar.add_cascade(label="File", menu=main_menu, font=40)

        editmenu = tk.Menu(menu_bar, tearoff=0)
        editmenu.add_command(label="Undo", command=self.not_implement, font=40)
        editmenu.add_command(label="Reset", command=self.not_implement, font=40)
        editmenu.add_command(label="Re-size (beta)", command=self.not_implement, font=40)
        editmenu.add_separator()
        editmenu.add_command(label="Rotate 90°C right", command= lambda: self.action_do(4), font=40)
        editmenu.add_command(label="Rotate 90°C left", command= lambda: self.action_do(5), font=40)
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
        self.root.config(menu=menu_bar, background='black')


