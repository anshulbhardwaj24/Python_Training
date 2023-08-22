thislist = ["abc", 34, True, 40, "male"]
thislist2 = list(("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"))

# accessing the list
print(len(thislist))
print(thislist2[1])
print(thislist2[2:5])

#member operator on list
print(34 in thislist)

#index accessing the list
thislist[0] = "xyz"
thislist2[1:3] = ["blackcurrant", "watermelon"]
thislist[1:2] = ["blackcurrant", "watermelon"]

# insert something in the list at an particular index or at end
thislist.insert(2,"Hello")
thislist.append("World")

#adding content of one list into another
thislist.extend(thislist2)

#remove and deleting operations
thislist.remove("male")
thislist.pop(0) 
thislist.pop()
del thislist[0]
thislist.clear()

# Looping on list
for i in thislist:
    print(i)

for i in range(len(thislist)):
    print(thislist[i])
# While looping
i = 0
while i<len(thislist):
    print(thislist[i])
    i = i+1

# List Comprehension
[print(x) for x in thislist2 if "a" in x]
newlist = [x.upper() for x in thislist2]
print(newlist)

# Sorting list
thislist2.sort()
thislist2.sort(reverse=True)

# Sorting Using Functions
def myfunc(n):
  return abs(n - 50)

thislist3 = [100, 50, 65, 82, 23]
thislist3.sort(key = myfunc)
print(thislist3)

#case senetive
thislist = ["banana", "Orange", "Kiwi", "cherry"]
print(thislist.sort()) # Capital words are sorted first than the small words
print(thislist.sort(key = str.lower)) #we can use this method to overcome this issue

# reversing the list not based on the sorting
print(thislist.reverse())

#copy of the lists
mylist = thislist.copy()
mylist = list(thislist)

#Join Lists
mylist = thislist + thislist2
thislist.extend(thislist2)
