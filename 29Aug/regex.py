import re

# return list if the element found in string
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

# turn the match object with matching string 
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)

# split the string based on the given element
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

# replace the element within the string with new element
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)


txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x)