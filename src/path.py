from pathlib import Path
# import os

windows_path_string = "C:\\Users\\username\\Documents\\file.txt"

# # Convert to a PurePosixPath object
# posix_path = PurePosixPath(windows_path_string)

# # Convert the object back to a string for use in a Linux environment
# linux_path_string = str(posix_path)

# print(linux_path_string)
# # Output: C:/Users/username/Documents/file.txt (Note: this handles the slashes, but not drive letters)

p = Path(windows_path_string)
print(p)

# posix = p.as_posix()
# print(posix)
print(p.name)