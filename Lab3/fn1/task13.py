import time

g_number = 0
m_name   = ""
status   = True
count    = 1

def generate_number():
    global g_number
    current_time = time.time()
    g_number     = int(current_time) % 20 + 1

def greeting(name : str):
    global m_name 
    m_name = name
    print(f"\nWell, {name}, I am thinking of number betweem 1 and 20.\nTake a guess.")

def chek_number(n : int):
    global status
    global count 
    g_n = g_number
    if g_n == n:
        print(f"\nGood joob, {m_name}!, You gusswed my number in {count} guesses!")
        status = False
    elif g_n < n:
        print("\nYour guess is too high.")
    else:
        print("\nYour guess is too low.")
    
    if status:
        count += 1
        print("Take a guess.")

name = input("Hello! What is your name?\n")
greeting(name)
generate_number()

while status:
    number = int(input(""))
    chek_number(number)
