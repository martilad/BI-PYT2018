from Operations import Operations
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image
import tkinter as tk
import os 


class GUI:
    def __init__(self):
        self.load = False
        # This creates the main window of an application
        self.root = tk.Tk()
        self.root.title("Semestr work")
        self.root.bind('<Control-z>', self.back)
        self.create_menu_to_root()
        self.image = Operations()
        display_text = tk.StringVar()
        display_text.set("Lets start...")

        # This create the main text without picture
        self.label = tk.Label(self.root, height=4, width=30, font=40, textvariable=display_text)
        self.label.pack()
    
        # Create empty picture box
        self.panel = tk.Label(self.root, image = None)
        
        """Start aplications"""
    def start(self):
        # Start the GUI
        self.root.mainloop()

        """Not implement function"""
    def not_implement(self):
        print("This function is not implemet...")

    def action_do(self, number):
        message = True
        if self.load:
            if number == 10: # reset image
                message = self.image.reset()
            if number == 11: # undo 
                message = self.image.pop()
            if number == 12: # resize
                message = self.image.reset()
            if number == 13: # turn right
                message = self.image.rotate_right()
            if number == 14: # turn left
                message = self.image.rotate_left()
            if number == 15: # mirror X
                message = self.image.mirror_x()
            if number == 16: # mirror Y
                message = self.image.mirror_y()
            if message != True:
                messagebox.showinfo("Error", message)
            self.image_to_window()

        """Back if is press ctrl-z"""
    def back(self, event):
        self.action_do(11)

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

        """Save to existing file"""
    def save_image(self):
        if self.load:
            message = self.image.save_image(self.root.filename)
            # Handle message if fail save file
            if message != True:
                messagebox.showinfo("Error", message)

        """Save to new file save dialog"""
    def save_image_to_new(self):
        message = ""
        dir_path = os.getcwd()
        self.root.filename =  tk.filedialog.asksaveasfilename(initialdir = dir_path,title = "Save file",filetypes = (("pictures","*.jpg *.png *.tiff *.bmp"),("all files","*.*")))
        if self.load:
            message = self.image.save_image(self.root.filename)
            # Handle message if fail save file
            if message != True:
                messagebox.showinfo("Error", message)
                self.root.filename = self.work_file
        # if fail back to last work file
        self.work_file = self.root.filename

        """Start aplications"""
    def load_file(self):
        dir_path = os.getcwd()
        self.root.filename =  tk.filedialog.askopenfilename(initialdir = dir_path,title = "Select file",filetypes = (("pictures","*.jpg *.png *.tiff *.bmp"),("all files","*.*")))
        load = self.image.load_image(self.root.filename)
        # Handle message if fail load file
        if load != True:
            messagebox.showinfo("Error", load)
            if self.load:
                self.root.filename = self.work_file
            return
        self.label.pack_forget()
        self.image_to_window()
        # if fail back to last work file
        self.load = True
        self.work_file = self.root.filename

        """Show about dialog"""
    def about_dialog(self):
        T = tk.Toplevel(self.root)
        display_text = tk.StringVar()
        label = tk.Label(T, height=4, width=30, font=40, textvariable=display_text)
        label.grid(row=4, columnspan=3)
        display_text.set("This app is created\n as semestral work \n in subject BI-PYT (Python)\
            \n on Faculty of Information Technology")

        """Init menu bar of aplication"""
    def create_menu_to_root(self):
        menu_bar = tk.Menu(self.root)

        main_menu = tk.Menu(menu_bar, tearoff=0)

        main_menu.add_command(label="Open", command=self.load_file, font=40)
        main_menu.add_command(label="Save", command=self.save_image, font=40)
        main_menu.add_command(label="Save as...", command=self.save_image_to_new, font=40)
        main_menu.add_separator()
        main_menu.add_command(label="Exit", command=self.root.quit, font=40)
        menu_bar.add_cascade(label="File", menu=main_menu, font=40)

        editmenu = tk.Menu(menu_bar, tearoff=0)
        editmenu.add_command(label="Undo", command= lambda: self.action_do(11), font=40)
        editmenu.add_command(label="Reset", command= lambda: self.action_do(10), font=40)
        editmenu.add_command(label="Re-size (beta)", command=self.not_implement, font=40)
        editmenu.add_separator()
        editmenu.add_command(label="Rotate 90°C right", command= lambda: self.action_do(13), font=40)
        editmenu.add_command(label="Rotate 90°C left", command= lambda: self.action_do(14), font=40)
        editmenu.add_separator()
        editmenu.add_command(label="MirroringX", command= lambda: self.action_do(15), font=40)
        editmenu.add_command(label="MirroringY", command= lambda: self.action_do(16), font=40)
        editmenu.add_command(label="Inverte", command= lambda: self.action_do(17), font=40)
        editmenu.add_separator()
        editmenu.add_command(label="Greyscale", command= lambda: self.action_do(18), font=40)
        editmenu.add_command(label="Dark", command= lambda: self.action_do(19), font=40)
        editmenu.add_command(label="Light", command= lambda: self.action_do(20), font=40)
        editmenu.add_command(label="Highlight", command= lambda: self.action_do(21), font=40)
        menu_bar.add_cascade(label="Operation", menu=editmenu, font=40)

        helpmenu = tk.Menu(menu_bar, tearoff=0)
        helpmenu.add_command(label="About...", command=self.about_dialog, font=40)
        menu_bar.add_cascade(label="Help", menu=helpmenu, font=40)
        self.root.config(menu=menu_bar, background='black')


