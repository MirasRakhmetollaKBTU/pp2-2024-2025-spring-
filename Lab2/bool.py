#### Boolean;

# Example 1
print(10 > 9)
print(10 == 9)
print(10 < 9)

# Example 2
a = 200
b = 33

if b > a:
   print("b is greater than a")
else:
   print("b is not greater than a")

# Example 3
print(bool("Hello"))
print(bool(15))

# Example 4
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

# Example 5
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

# Example 6
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

# Example 7
class myclass():
   def __len__(self):
     return 0

myobj = myclass()
print(bool(myobj))

# Example 8
def myFunction() :
   return True

print(myFunction())

# Examplr 9
def myFunction() :
    return True

if myFunction():
   print("YES!")
else:
   print("NO!")

# Example 10
x = 200
print(isinstance(x, int))