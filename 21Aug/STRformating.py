txt = "My Age is :{}"
age = 21

print(txt.format(age)) # My Age is :21

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price)) # I want to pay 49.95 dollars for 3 pieces of item 567