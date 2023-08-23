# while Loop
i = 1
while i < 6:
  if i==0:
    break
  elif i==4:
    i=i+1
    continue
  else:
    print(i) # 1235
  i=i+1
else:
  print("i is no longer less than 6")

# For Loop
fruits = ["apple", "banana", "cherry","orange","mango","Kiwi"]
LoopData=[]
for x in fruits:
  if x == "banana":
    continue
  elif x == "mango":
    break
  else:
    LoopData.append(x)
  for i in LoopData:
    pass
print(LoopData)  # ['apple', 'cherry', 'orange']