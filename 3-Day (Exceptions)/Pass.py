# implementing error using loop 

while True:
    try:
        x = int(input("Wnat's x ?  "))
    except ValueError:
        print("That's not a valid number!")
    else:
        break
print(f"x is {x}")

#implementing same concept using function

# pass 
# The pass keyword in Python is basically a placeholder. 
# It does nothing—literally. It’s used when you need to put something syntactically, 
# but you don’t want the code to do anything yet.



def main():

    x = get_int("What's X ? ")
    print(f"x is {x}")

def get_int(promrt):

    while True:
        try:
            return int(input(promrt))
        except ValueError:
            pass
main()