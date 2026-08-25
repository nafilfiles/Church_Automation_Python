import os
import pathvalidate as pv


# function to rename files, taking in the file path of old name and new name
def renamefile(oldname, newname):
    try:
        os.rename(oldname, newname)
    except FileNotFoundError:
        print(f"File '{oldname}' does not exist")
    except FileExistsError:
        print(f"Error: The file '{newname}' already exists.")
    except PermissionError:
        print("Error: Permission denied. Check file permissions.")
    except OSError:
        print("Bad characters")
    except OSError as e:
        print(f"An unexpected OS error occurred: {e}")
    except Exception as e:
         print(f"{e}")
        
def validation(string):
    #  print(pv.sanitize_filename(string))
    if string != pv.sanitize_filename(string, platform="auto") or string == "":
        return False
    else:
        return True

# input = input("enter a string")
# print(validation(input))