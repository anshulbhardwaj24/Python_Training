set1 = {"abc", 34, True, 40, "male"}
thisset = set(("apple", "banana", "cherry","Apple")) 

#accesing the sets
for x in thisset:
  print(x)

# Adding element in Sets
thisset.add("orange")
thisset.update(set1)

# Adding other than sets in set
mylist = ["kiwi", "orange"]
thisset.update(mylist)

# remove element in sets
thisset.remove("banana")
#  If the item to remove does not exist, remove() will raise an error.
thisset.discard("kiwi")
thisset.pop()
thisset.clear()
del thisset

# looping in sets
for x in thisset:
  print(x)

# Joining Sets
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.union(set2)

set1.intersection_update(set2) # to keep only duplicate in existing set
set1.intersection(set2) # to return a set that keep only duplicate

set1.symmetric_difference_update(set2) #inserts the symmetric differences from this set and another
set1.symmetric_difference(set2)  # Returns a set with the symmetric differences of two sets

print(set1.isdisjoint(thisset)) #True cause there is nothing common in both.

