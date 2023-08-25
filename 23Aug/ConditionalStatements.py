a = 300
b = 400
c = 700

# if , elif , else
if(a>b):
    print("A")
elif(b>c):
    print("b")
else:
    print("c")

# Short Hand If Else
print("A") if a > b else print("B")

# Conbining Conditional Statements
if b>c and b<c:
    print("And") #executes when both conditions are true
if a>b or b>a:
    print("Or") #Executes when any of the condition is true
if not a>b:
    print("not") # Executes when the condition is false but not turn it to true


