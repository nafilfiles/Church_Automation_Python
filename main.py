from functions.rename import renamefile
from functions.rename import validation

def main():
    print("Hello from church-automation-python!")
    old_name = input("Enter the file you want to rename: \n")
    while not validation(old_name):
        old_name = input("Filename contains forbidden characters\n")

    new_name = input("Enter the new name for the file: \n")
    while not validation(new_name):
        new_name = input("Filename contains forbidden characterswhat\n")
    # print(old_name)
    # print(new_name)
    renamefile(old_name, new_name)


if __name__ == "__main__":
    main()
