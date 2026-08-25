import tkinter as tk
from tkinter import filedialog

from dotenv import set_key

def input_vars():
    def browse_folder(entry_widget):
        folder_selected = filedialog.askdirectory()

        if folder_selected:
            entry_widget.delete(0, tk.END)
            entry_widget.insert(0, folder_selected)

    def submit():
        # get path variables from form and enter in .env file
        watchpath = watch_entry.get().replace('/', '\\')
        audiopath = audio_entry.get().replace('/', '\\')
        logpath = log_entry.get().replace('/', '\\')
        set_key(".env", "watchpath", watchpath)
        set_key(".env", "audiopath", audiopath)
        set_key(".env", "logpath", logpath)
        root.destroy()

    root = tk.Tk()
    root.title("Directory Input Form")
    root.geometry("650x250")

    # WATCH
    tk.Label(root, text="Watch Directory:").place(x=20, y=30)
    watch_entry = tk.Entry(root, width=60)
    watch_entry.place(x=180, y=30)

    tk.Button(
        root,
        text="Browse",
        command=lambda: browse_folder(watch_entry)
    ).place(x=560, y=26)

    # AUDIO
    tk.Label(root, text="Audio File Directory:").place(x=20, y=80)

    audio_entry = tk.Entry(root, width=60)
    audio_entry.place(x=180, y=80)

    tk.Button(
        root,
        text="Browse",
        command=lambda: browse_folder(audio_entry)
    ).place(x=560, y=76)

    # LOG
    tk.Label(root, text="Log Directory:").place(x=20, y=130)
    log_entry = tk.Entry(root, width=60)
    log_entry.place(x=180, y=130)
    tk.Button(
        root,
        text="Browse",
        command=lambda: browse_folder(log_entry)
    ).place(x=560, y=126)

    # SUBMIT
    tk.Button(
        root,
        text="Submit",
        command=submit
    ).place(x=300, y=190)

    root.mainloop()