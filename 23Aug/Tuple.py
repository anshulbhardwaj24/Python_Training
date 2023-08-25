tuple1 = ("abc", 34, True, 40, "male")
thistuple = tuple(("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"))

# Accessing the tuple
print(thistuple[2:5])
print(thistuple[-4:-1]) # ('orange', 'kiwi', 'melon')

# Changing tupple values
y = list(thistuple)
y.append("Rice")
thistuple = tuple(y)

y = ("Wheat",)
thistuple += y

#removing the Values from tuple and deleting the tuple
y = list(thistuple)
y.remove("apple")
del thistuple

# Unpacking the tuple values
(a, *b, c) = thistuple

# Loop through tuple
for x in thistuple:
  print(x)

i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

# Tuple Join
tuple3 = tuple1 + thistuple