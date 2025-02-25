import time
import math

number = int(input("Enter number : "))
times  = float(input("Enter milliseconds : "))
time.sleep(times/1000)
svalue = math.sqrt(number)
print(f"Square root of {number} after {times} is {svalue}")
