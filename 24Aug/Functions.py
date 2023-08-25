# normal function
def my_function(Parameter):
  print(Parameter + " Refsnes")

argument = "Emili"
my_function(argument)

# If the no of arg is unknown we use *
def my_function(*MultipleParamters):
    print("The youngest child is " + MultipleParamters[2] + MultipleParamters[1])

multiple_Arguments = ["Emil", "Tobias", "Linus"]
my_function(multiple_Arguments)

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

# Keyword Argument
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#if the no of keyword arg is unknown  we us **
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

# defining default parameter value
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden") # prints sweden
my_function() #norway