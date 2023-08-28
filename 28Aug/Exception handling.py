# Python program to handle simple runtime error
 
a = [1, 2, 3]
try:
    print ("Second element = %d" %(a[1]))
 
    # Throws error since there are only 3 elements in array
    print ("Fourth element = %d" %(a[3]))
 
except:
    print ("An error occurred")


# raising an particular exception
def fun(a):
    if a < 4:
 
        # throws ZeroDivisionError for a = 3
        b = a/(a-3)
        
 
    # throws NameError if a >= 4
    print("Value of b = ", b)
    print("Value of b = ", c)
     
try:
    fun(3)
    fun(5)
except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")
except NameError:
    print("NameError Occurred and Handled")



# finally keyword 
# No exception Exception raised in try block
try:
    k = 5//0  # raises divide by zero exception.
    print(k)
 
# handles zerodivision exception
except ZeroDivisionError:
    print("Can't divide by zero")
 
finally:
    # this block is always executed
    # regardless of exception generation.
    print('This is always executed')


# raise keyword
try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print ("An exception")
