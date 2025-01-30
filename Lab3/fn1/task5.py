import itertools

def oprate(word : str):
    for letter in itertools.permutations(word):
        print(''.join(letter))
    
    return

word = input("Enter toyr word")
oprate(word)