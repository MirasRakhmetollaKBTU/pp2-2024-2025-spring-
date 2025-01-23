### Touples

# Example 1
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Example 2
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# Example 3
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# Example 4
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

# Example 5
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

# Example 6
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

# Example 7
tuple1 = ("abc", 34, True, 40, "male")

# Example 8
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

# Example 9
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

# Example 10
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# Example 11
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

# Example 12
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

# Example 13
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

# Example 14
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

# Example 15
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

# Example 16
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

# Example 17
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# Example 18
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

# Example 19
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

# Example 20
fruits = ("apple", "banana", "cherry")

# Example 21
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# Example 22
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

# Example 23
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

# Example 24
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

# Example 25
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

# Example 26
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

# Example 27
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# Example 28
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

# Example 29
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

# Example 30
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists