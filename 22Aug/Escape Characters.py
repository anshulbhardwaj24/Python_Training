txt = 'It\'s alright.'
txt1 = "This will insert one \\ (backslash)."
txt2 = "Hello\nWorld!"
txt3 = "Hello\rWorld!"
txt4 = "Hello\tWorld!"
txt5 = "Hello \bWorld!"
txt6 = "\x48\x65\x6c\x6c\x6f"

print(txt)  # It's alright.
print(txt1) # This will insert one \ (backslash).
print(txt2) #Hello
            #World!

print(txt3)  #Hello
             #World!

print(txt4)   # Hello	World!
print(txt5)   # HelloWorld!
print(txt6)   # Hello