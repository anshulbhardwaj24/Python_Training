thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"],
}

thisdict1 = dict(name = "John", age = 36, country = "Norway")

#Accesing Dictionary 
x = thisdict["colors"]
x = thisdict.get("colors")
x = thisdict.keys()
x = thisdict.values()
x = thisdict.items()

# changing item
thisdict.update({"year": 2020})
# adding item
thisdict["color"] = "red"
thisdict.update({"color": "red"})
x = thisdict.setdefault("model", "Bronco")
# removing item
thisdict.pop("model")
thisdict.popitem() #remove the last inserted item
del thisdict["model"]
thisdict.clear()

# coping
mydict = thisdict.copy()
mydict = dict(thisdict)

