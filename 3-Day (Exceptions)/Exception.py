# is basically an error that occurs during the execution of a program,
#  which disrupts the normal flow of instructions

# SyntaxError
#  is an error that occurs when the syntax of a program is incorrect or
#  invalid, which prevents the program from running

"""
x = int(input("What's x )) 
- This line of code will raise a SyntaxError because 
- there is an extra closing parenthesis at the
"""

# ValueError
#  is an error that occurs when a function or operation receives an argument
#  with an incorrect value, which prevents the function or operation from working correctly

#  For example, if you try to convert a string to an integer using the int() function
#  and the string contains non-numeric characters, a ValueError will be raised

try:
    x = int(input("What's x "))
    print("You entered:", x)
except ValueError:
    print("That's not a valid number!")

    
# NameError
#  is an error that occurs when a variable or function is used before it has been defined
#  or when a variable or function is used with a name that has not been assigned to it
#  For example, if you try to print a variable that has not been defined, 
#  a NameError will be raised

try:
    x = int(input("What's X ?  "))
except ValueError:
    print("That's not a valid number!")
print(f"x is {x}") #if x is not defined, this will raise a NameError, incase of exception

#  we can use the else block to handle this case
try:
    x = int(input("What's x "))
except ValueError:
    print("That's not a valid number!")
else:
    print(f"x is {x}") #this will only run if the try block does not rais