videoinfo = [
    "Pastor So n So",
    "A good sermon",
    "12-23-25 12:35:52",
    "path",
    "wooooow"
]

# New file with data from videoinfo variable
with open("log.txt", "w") as file:
    for i in range(len(videoinfo)):
        file.write(f"{videoinfo[i]}\n")
    file.write("end!")
