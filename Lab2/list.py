### list

# Example 15
thislist = ["apple", "banana", "cherry"]
print(thislist)

# Example 16
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# Example 17
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# Example 18
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

# Example 19
list1 = ["abc", 34, True, 40, "male"]

# Example 20
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

# Example 21
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

# Example 22
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# Example 23
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# Example 24
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

# Example 25
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

# Example 26
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

# Example 27
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

# Example 28
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
   print("Yes, 'apple' is in the fruits list")

# Example 29
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# Example 30
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# Example 31
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

# Example 32
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

# Example 33
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

# Example 34
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# Example 35
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# Example 36
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# Example 37
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# Example 38
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# Example 39
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

# Example 40
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# Example 41
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# Example 42
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# Example 43
thislist = ["apple", "banana", "cherry"]
del thislist

# Example 44
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# Example 45
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

# Example 46
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
   print(thislist[i])

# Example 47
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
   print(thislist[i])
   i = i + 1

# Example 48
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

# Example 49
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
   if "a" in x:
    newlist.append(x)
print(newlist)

# Example 50
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

# Example 51
newlist = [x for x in fruits if x != "apple"]

# Example 52
newlist = [x for x in range(10)]

# Example 53
newlist = [x for x in range(10) if x < 5]

# Example 54
newlist = [x.upper() for x in fruits]

# Example 55
newlist = [x.upper() for x in fruits]

# Example 56
newlist = [x if x != "banana" else "orange" for x in fruits]

# Example 57
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# Example 58
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# Example 59
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

# Example 60
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

# Example 61
def myfunc(n):
   return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

# Example 62
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

# Example 63
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

# Example 64
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

# Example 65
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Example 66
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# Example 67
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

# Example 68
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# Example 69
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
   list1.append(x)

print(list1)

# Example 70
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)