videoinfo = [
    "Pastor So n So",
    "A good sermon",
    "12-23-25 12:35:52",
    "path",
    "wooooow"
]

# Open a file in write mode ('w') and write a single string
with open("log.txt", "w") as file:
    for i in range(len(videoinfo)):
        file.write(f"{videoinfo[i]}\n")
    file.write("end!")
# The file is automatically closed after the 'with' block is executed
