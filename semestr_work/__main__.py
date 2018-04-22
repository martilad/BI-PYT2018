import tkinter as tk
from PIL import ImageTk, Image
    
def write_slogan():
    print("Tkinter is easy to use!")

def donothing():
   filewin = tk.Toplevel(root)
   button = tk.Button(filewin, text="Do nothing button")
   button.pack()

"""root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="Hello",
                   command=write_slogan)
slogan.pack(side=tk.LEFT)

root.mainloop()"""

#This creates the main window of an application
root = tk.Tk()
root.title("Join")
#window.geometry("600x600")
#window.configure(background='black')

menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = tk.Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar, background='black')


path = "test.png"
size = 500, 500
im_temp = Image.open(path)
im_temp = im_temp.resize(size, Image.ANTIALIAS)
#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(im_temp)

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(root, image = img)

#The Pack geometry manager packs widgets in rows or columns.
panel.pack(side = "right", fill = "both", expand = "yes")

#Start the GUI
root.mainloop()