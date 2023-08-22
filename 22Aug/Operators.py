 # Arithmetic Operators
print(5+2) # add the variable = 7
print( 5-2) # substract = 3
print( 5*2) # multiply = 10
print( 5/2) # divide = 2.5
print( 5%2) # modulus = 1 
print( 5**2) # power = 5*5 = 25
print( 15//2) # floor = 7 (nearest whole number)



#Assignment Operators 
x = 2         # 2    lets take it as x default value
x = x+3       # 5
x += 3        # 5
x -+ 3        # -1
x **= 3       # 8



# comparision Operators 
print(3 == "3")  #true
print(3 > 5)  #False
print(4>=3)  #true
print(3!=2)  #true



#Logical Operators
print(3>2 and 4>3)  #true cause both statement are ture
print(2>3 and 4>3)  #False cause both statement are not ture

print(3>2 or 4>3)  #true cause both statement are ture
print(2>3 or 4>3)  #true cause one statement is true
print(2>3 or 3>4)  #False cause none of the statement are true

print(not(2>3 and 4>3) ) # return true cause its return false
print(not(3>2 or 4>3) ) # return false cause it returns the true




# Identity Operators
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z) # true
print(x is y) # flase
print(x ==y ) # true

print(x is not z) #flase
print(x is not y) # true

# membership Operators
x = ["apple", "banana"]
print("apple" in x) #true
print("apple" not in x) #flase


# Bitwise Operators
print(6 & 3) # = 2 # AND - Sets each bit to 1 if both bits are 1
print(6 & 3) # = 7 # OR - Sets each bit to 1 if one of two bits is 1
print(6 ^ 3) # = 5 # XOR - Sets each bit to 1 if only one of two bits is 1
print(~3) # = -4 # NOT - Inverts all the bits
print(3 << 2) # = 12 # Zero fill left shift - Shift left by pushing zeros
                #in from the right and let the leftmost bits fall off
print(8 >> 2) # = 2 # Signed right shift - Shift right by pushing copies of
                #the leftmost bit in from the left, and let the rightmost bits fall off