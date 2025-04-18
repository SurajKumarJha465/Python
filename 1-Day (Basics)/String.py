#differnt function defined under string 

name = input("What is your name? ")

""""
Input : What is your name?         Suraj jha
"""

#removes the whitespace form string 
name = name.strip()

#capitalize the first letter of the string
name = name.capitalize()

#capitalize the Each letter of the string and make the rest lowercase
name = name.title()


print("Hello,",name) 
""""
#output: Hello, Suraj
"""

#combine all the string functions together
name = input("What is your name? ").strip().capitalize().title()

#split the string into list of words
words = name.split()
print(words) #output: ['Hello,', 'Suraj']