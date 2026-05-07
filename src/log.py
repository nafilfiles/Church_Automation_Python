# New file with data from videoinfo variable
from datetime import datetime

def create_log(videoinfo, logpath):
    with open(f"{logpath}\\log.txt", "w") as file:
        for i in range(len(videoinfo)):
            file.write(f"{videoinfo[i]}\n")
        now = datetime.now()
        datestring = now.strftime("%Y-%m-%d %H:%M:%S") 
        file.write(datestring)
    print("Log File created successfully")
