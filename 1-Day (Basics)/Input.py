# program to take input from user and display

# the input on the screen
name = input ("What is your name? ")

#print name on the screen using print function(+)
print("Hello, " + name)

#print name on the screen using print function(,)
print("\n")
print("Hello,",name)

#special string f
print(f"Hello, {name}")

#working of print function
print("Hello, " , end = "")
print(name)

#for seperator 
print("Hello,",name, sep="  ")

#print "" inside the ""
print("Hello, \"friend\"")
#or 
print('Hello, "Friend"')