import os

def check_path_for_every_think(path):
    if os.path.exists(path):
        print(f"The path '{path}' exists.")
    else:
        print(f"The path '{path}' do not exists.")
    
    if os.access(path, os.R_OK):
        print(f"The path '{path}' readable.")
    else:
        print(f"The path '{path}' is not readable.")

    if os.access(path, os.W_OK):
        print(f"The path '{path}' writable.")
    else:
        print(f"The path '{path}' writable.") 

    if os.access(path, os.X_OK):
        print(f"The path '{path}' executable.") 
    else:
        print(f"The path '{path}' is not executable.")

def main():
    path = input("Enter the path : ")
    check_path_for_every_think(path)

if __name__ == "__main__":
    main() 