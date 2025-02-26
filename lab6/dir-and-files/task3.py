import os

def check_path(path):
    if os.path.exists(path):
        print(f"The path '{path}' exists.")
        if os.path.isdir(path):
            dirs     = path.split('/')
            dirIneed = dirs[-1]
            
            del dirs
            
            print(f"'{dirIneed}' is directory")

            return True
        else:
            print(f"'{dirIneed}' is not directory")
            return False
    else:
        print(f"The path '{path}' does not exists.")
        return False

def check_files(path, file_name):
       if os.path.exists(path + "/" + file_name):
            print(f"The file'{file_name}' exists.")
            return True
       else:
            print(f"The file'{file_name}' is not exists.")
            return False

def main():
    path = input("Enter path : ")
    if check_path(path):
        file_name = input("Enter your file : ")
        check_files(path, file_name)

if __name__ == "__main__":
    main()
