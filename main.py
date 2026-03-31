from src import rename
import pathvalidate as pv


import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import tkinter as tk
from tkinter import simpledialog

import re

def main():
  class MyEventHandler(FileSystemEventHandler):
      def __init__(self):
          self.actionstack = ""
      def on_any_event(self, event):
          self.actionstack += event.event_type[0]
          # print(self.actionstack)
          if re.search(r"c\w*d\w*c\w*m", self.actionstack):
              self.actionstack = ""
              fullpath = event.src_path
              string = event.src_path.rsplit("\\", maxsplit=1)[0]
              # print(string)
              # create a hidden main window
              root = tk.Tk()
              root.withdraw() 

              # open the prompt dialog
              user_input = ""
              while user_input == "":
                user_input = simpledialog.askstring("Input", "Input new file name",
                                      parent=root)
                
              rename.renamefile(fullpath, f"{string}\\{user_input}")


    
  # Set up the observer and event handler
  event_handler = MyEventHandler()
  observer = Observer()
  # Watch the current directory ('.') recursively
  observer.schedule(event_handler, r'C:\Users\nickh\Desktop\watch', recursive=True) 

  # Start the observer
  observer.start()
  try:
      while True:
          time.sleep(1) # Sleep to prevent high CPU usage
  except KeyboardInterrupt:
      observer.stop()
  observer.join()

# class Video:
#   def __init__(self, date, title, speaker):
#     self.date = date
#     self.title = title
#     self.speaker = speaker

#   def showtitle(self):
#     print(self.title)

# def main():
    # old_name = ""
    # print("Hello from church-automation-python!")
    # # old_name = input("Enter the file you want to rename: \n")
    # while not pv.is_valid_filename(old_name):
    #     print("Filename contains forbidden characters")
    #     old_name = input("Enter the file you want to rename:\n")

    # new_name = input("Enter the new name for the file: \n")
    # while not pv.is_valid_filename(new_name):
    #     new_name = input("Filename contains forbidden characters\n")
    # # print(old_name)
    # # print(new_name)
    # rename.renamefile(old_name, new_name)

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
