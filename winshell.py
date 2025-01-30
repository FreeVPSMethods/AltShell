import tkinter as tk
import subprocess

def open_command_prompt():
    # Open Command Prompt
    subprocess.Popen('cmd.exe')

def shellcreate():
    # Create the main window
    window = tk.Tk()
    window.attributes('-fullscreen', True)

    # Create a menubar
    menubar = tk.Menu(window)

    # Create a File menu
    file_menu = tk.Menu(menubar, tearoff=0)
    file_menu.add_command(label="Open Command Prompt", command=open_command_prompt)
    
    # Add the File menu to the menubar
    menubar.add_cascade(label="File", menu=file_menu)

    # Configure the window to use the menubar
    window.config(menu=menubar)

    # Optionally, bind the Escape key to exit fullscreen mode
    window.bind("<Escape>", lambda event: window.attributes('-fullscreen', False))

    # Add a label for demonstration purposes
    label = tk.Label(window, text="Welcome to the Fullscreen Shell", font=("Helvetica", 24))
    label.pack(expand=True)

    # Start the main loop
    window.mainloop()

if __name__ == "__main__":
    shellcreate()
