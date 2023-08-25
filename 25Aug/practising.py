a =[1,2,3,4,5,6]
b=[]
for i in a:
    b.append((i,i*i))

print(b)

# list of all keys
dict1 = {
    "one":1,
    "two":2,
    "three":3
}
print(list(dict1.keys()))

# set to tuple using list comprehension
a = {1,2,3,4,5}
x = tuple([x for x in a])
print(x)


# dictonary to list of student above 18
student_ages = {
    "Alice": 20,
    "Bob": 22,
    "Charlie": 18,
    "David": 25
}
above_18_students = [{name:age} for name, age in student_ages.items() if age > 18]
print(above_18_students[0]['Alice'])

# list of tuples containing item of another list 
names = ["Alice", "Bob", "Charlie"]
greetings = [('Hellow',name) for name in names]
print(greetings)

# word frequency
sentence = "This, is a, sample sentence, is a"
word_frequency = {}
words = sentence.split(',')
for word in words:
    word_frequency[word] = word_frequency.get(word, 0) + 1
print(word_frequency)


list2 = [ ('apple' , 0), ('grape', 1), ('watermelon', 2), ('orange', 3)]
dict2 = dict(list2)
print(dict2)






list1 = [1, 2, 2, 3, 4, 4, 5]
sq = list(map(lambda x: x**2 , list1))
print(sq)