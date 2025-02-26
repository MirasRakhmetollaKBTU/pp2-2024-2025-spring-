import os

def list_directories(path):
    try:
        directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path,d))]
        return directories
    except FileNotFoundError:
        return f"path '{path}' is not found."
    except PermissionError:
        return f"permission denied to acces '{path}'."
    
def list_files(path):
    try:
        files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
        return files
    except FileNotFoundError:
        return f"path '{path}' is not found."
    except PermissionError:
        return f"path '{path}' is denied to acces by permission."

def list_all(path):
    try:
        all_items = os.listdir(path)
        return all_items
    except FileNotFoundError:
        return f"path '{path}' is not found."
    except PermissionError:
        return f"path '{path}' is denied to access by permission."

def main():
    path = input("Enter the path to list the contents : ")
    
    print("\nDirectories : ")
    directories = list_directories(path)
    print(directories)

    print("\nFiles : ")
    files = list_files(path)
    print(files)

    print("\nAll directories and files: ")
    all_items = list_all(path)
    print(all_items)

if __name__ == "__main__":
    main()
