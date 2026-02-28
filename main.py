from src import rename
import pathvalidate as pv

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


if __name__ == "__main__":
    main()
