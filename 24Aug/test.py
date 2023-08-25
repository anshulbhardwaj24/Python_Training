a =[1,2,3,4,5,6]
b=[]
for i in a:
    b.append((i,i*i))

print(b)




people = [{'name': 'Alice', 'age': 30}, {'name': 'Charlie', 'age': 25}, {'name': 'Bob', 'age': 25}]
sort = tuple(sorted(people, key=lambda x: (x['age'], x['name'])))
print("Sorted people:", sort)