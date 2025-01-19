# example 1
print ("Hello world")

# example 2
import sys
print(sys.version)

# example 3
if 5 > 2:
    print ("Five is greater than two")

# example 4
if 5 > 2:
        print ("Five is greater than two")

if 5 > 2:
   print ("Five is greater than two")

# example 5
#this is a comment
print ("Hello world")

# example 6
print ("Hello world") #this is a comment

# example 7
#print ("Hello world")
print ("Hello, world")

# example 8
print ("Cheers, Mate!")

# example 9
#This is a comment
#writte in 
#more than just one line
print ("Hello world")

# example 10

"""

This is a comment
written in 
more than just one line

"""

print ("Hello world")

# example 11
x = 5
y = "John"
print (x)
print (y)

# example 12
x1 = 4
x1 = "Sally"
print (x)

# example 13
x2 = str   (3)
y2 = int   (3)
z2 = float (3)

#example 14
x3 = 5
y3 = "John"
print(type (x3))
print(type (y3))

# example 15
x4 = "Jhon"
#is the same as 
x4 = 'John'

# example 16
myvar   = "Jhon"
my_var  = "Jhon"
_my_var = "Jhon"
myVar   = "Jhon"
MYVAR   = "Jhon"
myvar2  = "Jhon"

# example 17
x5, y5, z5 = "Orange", "Banana", "Cherry"
print (x5)
print (y5)
print (z5)

# example 18
x6 = y6 = z6 = "Orange"
print (x6)
print (y6)
print (z6)

# example 19
fruits = ["apple", "banana", "cherry"]
x7, y7, z7 = fruits
print (x7)
print (y7)
print (z7)

# example 20
x8 = "Python is awesome"
print (x8)

# example 21
x9 = "Python"
y9 = "is"
z9 = "awesome"
print (x9, y9, z9)

# example 22
x9 = "Python"
y9 = "is"
z9 = "awesome"
print (x9 + y9 + z9)

# example 23
x10 = 5
y10 = "jhon"
print(x10, y10)

# example 24
x11 = "awesome"
def myFunct():
     print ("Python is " + x11)

myFunct()

# example 25
x12 = "awesom"
def myFunct1():
     x = "Fantastic"
     print ("Pyrhin is " + x12)
myFunct1()
print ("Python is " + x12)

# example 26
x13 = "awesom"
def myFunct2():
     global x13
     x13 = "fantastix"
myFunct2()
print ("Python is " + x13)

# example 27
x14 = 1   #int
y14 = 2.8 #float
z14 = 1j  #complex

# example 28 int
x15 = 1
y15 = 7439027892307502
z15 = -749827342742

print(type(x15))
print(type(y15))
print(type(z15))

# example 29 float
x16 = 1.10
y16 = 1.0
z16 = -35.423

print(type(x16))
print(type(y16))
print(type(z16))

# example 30
x17 = 32e3
y17 = 12E4
z17 = -8724.7329e100

# example 31
x18 = int (1)
y18 = int (2.8)
z18 = int ("3")

# example 32
x19 = float (1)
y19 = float (2.8)
z19 = float ("3")
w19 = float ("3.1")

# example 33
x20 = str ("s1")
y20 = str (2)
z20 = str (3.9)

# example 34
print("Hello")
print('Hello')

# example 35
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

# example 36
a = "Hello"
print(a)

# example 37
a1 = """Lorem inpsum dolor sit amet,
        consectetur adipiscing elit,
        ut labore et dolore magna aliqua."""
print (a1)

# example 38
a2 = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a2)

# example 39
b = "Hello, World!"
print (b[2 : 5])

# example 40
b1 = "Hello, World1"
print (b[ : 5])

# example 41
b2 = "Hello, World!"
print(b[2 : ])

# example 42
b3 = "Hello, World!"
print(b[-5 : -2])

# example 43
a3 = "Hello, world!"
print(a3.upper())

# example 44
a4 = "Hello, World!"
print(a4.lower())

# example 45
a5 = " Hello, World! "
print(a5.strip()) # returns "Hello, World!"

# example 46
a6 = "Hello, World!"
print(a6.replace("H", "J"))

# example 47
a7 = "Hello, World!"
print(a7.split(",")) # returns ['Hello', ' World!']

# example 48
a8 = "Hello"
b8 = "World"
c8 = a8 + b8
print(c8)

# example 49
a9 = "Hello"
b9= "World"
c9 = a9 + " " + b9
print(c9)

# example 50
age = 36
txt = f"My name is John, I am {age}"
print(txt)

# example 51
price = 59
txt = f"The price is {price} dollars"
print(txt)

# example 52
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

# example 53
txt = f"The price is {20 * 59} dollars"
print(txt)

# example 54
txt = "We are the so-called \"Vikings\" from the north."