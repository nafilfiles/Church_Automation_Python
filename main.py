
# from src.youtube import Video

# from datetime import datetime
import time
import os
import re
from dotenv import load_dotenv
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import tkinter as tk
from src.rename import renamefile
from src.env_vars import input_vars
from src.audio_extract import extract_audio
from src.log import create_log
from src.ytupload import authenticate_youtube, upload_video

# load path variables from dotenv
load_dotenv()
watchpath = os.getenv("watchpath")
audiopath = os.getenv("audiopath")
logpath = os.getenv("logpath")

# trigger path input dialog if any path variable is not found
if watchpath is None or audiopath is None or logpath is None:
    input_vars()
    load_dotenv()

# main script functions w/ file watcher
def main():
  class MyEventHandler(FileSystemEventHandler):
      def __init__(self):
          self.actionstack = ""
          
      def on_any_event(self, event):
          # look for video made by OBS
          self.actionstack += event.event_type[0]
          print(self.actionstack)
          if re.search(r"c\w*d\w*c\w*m", self.actionstack):
              # clear actionstack on trigger
              self.actionstack = ""
              fullpath = event.src_path
              string = event.src_path.rsplit("\\", maxsplit=1)[0]

              def submit():
                title = title_entry.get()
                speaker = speaker_entry.get()
                # rename file
                renamefile(fullpath, f"{string}\\{title} - {speaker}.mkv")

                # upload to youtube
                youtube = authenticate_youtube()
                upload_video(youtube, f"{title} - {speaker}")

                # extract audio
                extract_audio(f"{string}\\{title} - {speaker}.mkv", f"{audiopath}\\{title} - {speaker}.mp3")

                # define log file data and create log file
                videoinfo = [title, speaker, fullpath]
                create_log(videoinfo, logpath)
                
                root.destroy()

              # Create main window
              root = tk.Tk()
              root.title("Input Form")
              root.geometry("300x150")

              # Title label and entry
              title_label = tk.Label(root, text="Title")
              title_label.pack()
              title_entry = tk.Entry(root, width=30)
              title_entry.pack()
              # Speaker label and entry
              speaker_label = tk.Label(root, text="Speaker")
              speaker_label.pack()
              speaker_entry = tk.Entry(root, width=30)
              speaker_entry.pack()

              # Submit button
              submit_button = tk.Button(root, text="Submit", command=submit)
              submit_button.pack(pady=10)

              # Run the app
              root.mainloop()
            
  # Set up the observer and event handler
  event_handler = MyEventHandler()
  observer = Observer()
  # Watch the current directory ('.') recursively
  observer.schedule(event_handler, watchpath, recursive=True) 
  print(watchpath)

  # Start the observer
  observer.start()
  try:
      while True:
          time.sleep(1) # Sleep to prevent high CPU usage
  except KeyboardInterrupt:
      observer.stop()
  observer.join()

if __name__ == "__main__":
    main()
