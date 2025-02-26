import os

def delete_file(path):
    if not os.path.exists(path):
        print(f"The path '{path}' is not found.")
        return

    if not os.access(path, os.W_OK):
        print(f"Permession denied to delete '{path}'.")
        return

    try:
        os.remove(path)
        print(f"File '{path}' is deleted succesfully")
    except:
        print(f"It can not be deleted '{path}'. Reson {Exception}")

def main():
    path = input("Enter path to delete : ")
    delete_file(path)

if __name__ == "__main__":
    main()
