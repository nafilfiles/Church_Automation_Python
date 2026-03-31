from src import rename
import pathvalidate as pv

class Video:
  def __init__(self, date, title, speaker):
    self.date = date
    self.title = title
    self.speaker = speaker

  def showtitle(self):
    print(self.title)

def main():
    old_name = ""
    print("Hello from church-automation-python!")
    # old_name = input("Enter the file you want to rename: \n")
    while not pv.is_valid_filename(old_name):
        print("Filename contains forbidden characters")
        old_name = input("Enter the file you want to rename:\n")

    new_name = input("Enter the new name for the file: \n")
    while not pv.is_valid_filename(new_name):
        new_name = input("Filename contains forbidden characters\n")
    # print(old_name)
    # print(new_name)
    rename.renamefile(old_name, new_name)

    # import tkinter as tk
    # from tkinter import simpledialog

    # # create a hidden main window
    # root = tk.Tk()
    # root.withdraw() 

    # # open the prompt dialog
    # user_input = simpledialog.askstring("Input", "What is your name?",
    #                                 parent=root)

    # # display the result
    # if user_input is not None:
    #     print(f"Hello, {user_input}!")
    #     video_data = user_input.split(",")
    #     v1 = Video(video_data[0], video_data[1], video_data[2])
    #     v1.showtitle()
    # else:
    #     print("No name entered.")


if __name__ == "__main__":
    main()
