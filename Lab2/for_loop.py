### For_loop

# Example 1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  
# Example 2
for x in "banana":
  print(x)
  
# Example 3
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

# Example 4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

# Example 5
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

# Example 6
for x in range(6):
  print(x)

# Example 7
for x in range(2, 6):
  print(x)
  
# Example 8 
for x in range(2, 30, 3):
  print(x)
  
# Example 9
for x in range(6):
  print(x)
else:
  print("Finally finished!")
  
# Example 10
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!") #this part of code doesn't work

# Example 11
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
    
# Example 12
for x in [0, 1, 2]:
  pass