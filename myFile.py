#Sets
a = {112, 114, 116, 118,112, 115}
a.add(119) # it's mutable

print(a) # the second 112 has been removed

#frozenSet
y = frozenset({"apple", "banana", "cherry"})
y.add("mango") #it shows error cause its immutable

#display x:
print(y)