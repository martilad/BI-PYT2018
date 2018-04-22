from GUI import GUI, tk
    

#This creates the main window of an application
root = tk.Tk()
root.title("Semestr work")
gui = GUI(root)
gui.create_menu_to_root(root)


#Start the GUI
root.mainloop()