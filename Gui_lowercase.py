import os
import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
from tkinter import filedialog, messagebox

def lowercase_rename(files):
    """Rename the files to lowercase."""
    for file_path in files:
        directory, filename = os.path.split(file_path)
        new_filename = filename.lower()
        new_filepath = os.path.join(directory, new_filename)
        os.rename(file_path, new_filepath)
    messagebox.showinfo("Success", "Files have been renamed to lowercase!")

def on_drop(event):
    """Handle the drop event."""
    files = root.tk.splitlist(event.data)
    lowercase_rename(files)

def ask_directory():
    """Allow the user to select a directory and rename all files within it to lowercase."""
    directory = filedialog.askdirectory()
    if directory:
        files = [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        lowercase_rename(files)

# Create the main window using TkinterDnD
root = TkinterDnD.Tk()
root.title("Lowercase File Renamer")

# Set up drag and drop area
drop_frame = tk.Label(root, text="Drag and drop files here or click to select directory", width=60, height=10, bg="lightgrey")
drop_frame.pack(padx=10, pady=10)
drop_frame.drop_target_register(DND_FILES)
drop_frame.dnd_bind('<<Drop>>', on_drop)
drop_frame.bind("<Button-1>", lambda e: ask_directory())

# Run the application
root.mainloop()
