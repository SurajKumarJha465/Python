# files or codes that other people can understand and use which is created by someone else is known as library

# we can use library in our code to make it more efficient and easy to understand
# we can import library in our code using import keyword



# random.choice(list) is used to choise any random element from the list


import random

coin = random.choice(["head","tail"])
print(coin)

# use of from keywords

from random import choice
coin = choice(["Head","Tail"])

# to generate random number form the given range
# we can use random.randint(a,b) function in python

number = random.randint(1,10)
print(number)


# to generate random float number between the given range
# we can use random.uniform(a,b) function in python 

number = random.uniform(1,10)
print(number)

# to suffle the list we can use random.shuffle(list) function in python

name = ["Suraj","Sumit","Dip","Animika","Amit"]

random.shuffle(name)
print(name)

for i in name:
    print(i)