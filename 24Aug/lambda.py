# lambda arguments : expression
# Lambda Function with multiple arg and one expression
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

# Lambda Function 
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

# Example of lambda function using if-else
Max = lambda a, b : a if(a > b) else b
 
print(Max(1, 2))

# lambda with list comprehension
new_list = [lambda arg=x: arg * 10 for x in range(1, 5)]

a = list(filter(lambda x: x%2 != 0, [1,2,3,4,5,6]))
 
# iterate on each lambda function
# and invoke the function to get the calculated value
for item in new_list:
    print(item())





thislist2 = list(("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"))
[print(x) for x in thislist2 if "a" in x]
