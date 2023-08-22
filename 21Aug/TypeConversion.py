#implicit conversion
a = 10  #int
b = 10.20  #float
c = a+b
print(type(c))  #float

# explicit conversion
x = 10
print(type(x)) #int

x= str(x)
print(type(x)) #str - string