import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyEventHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        if event.event_type == "modified":
            print(f'Event type: {event.event_type} | Path: {event.src_path}')
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