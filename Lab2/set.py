### SETS

# Example 1
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

# Example 2
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

# Example 3
thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)

# Example 4
thisset = {"apple", "banana", "cherry"}

print(len(thisset))

# Example 5
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

# Example 6
set1 = {"abc", 34, True, 40, "male"}

# Example 7
myset = {"apple", "banana", "cherry"}
print(type(myset))

# Example 8
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

# Example 9
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

# Example 10
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

# Example 11
thisset = {"apple", "banana", "cherry"}

print("banana" not in thisset)

# Example 12
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

# Example 13
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

# Example 14
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

# Example 15
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

# Example 16
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

# Example 17
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

# Example 18
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

# Example 19
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)

# Example 20
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

# Example 21
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

# Example 22
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)

# Example 23
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

# Example 24
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset)

# Example 25
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)

# Example 26
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

# Example 27
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

# Example 28
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)

# Example 29
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)

# Example 30
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)

print(set3)

# Example 31
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)

# Example 32
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)

# Example 33
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1)

# Example 34
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)

# Example 35
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)

# Example 36
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)