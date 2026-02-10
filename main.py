from functions.rename import renamefile
import pathvalidate as pv

def main():
    print("Hello from church-automation-python!")
    old_name = input("Enter the file you want to rename: \n")
    while old_name != pv.sanitize_filename(old_name, platform="auto") or old_name == "":
        old_name = input("Filename contains forbidden characters\n")

    new_name = input("Enter the new name for the file: \n")
    while new_name != pv.sanitize_filename(new_name, platform="auto") or new_name == "":
        new_name = input("Filename contains forbidden characterswhat\n")
    # print(old_name)
    # print(new_name)
    renamefile(old_name, new_name)


if __name__ == "__main__":
    main()
