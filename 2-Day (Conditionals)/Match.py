# use of match simillar to switch

name = input("What's your name : ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Welcome, Gryffindor!")
    case "Draco" | "Pansy" | "Blaise":
        print("Welcome, Slytherin!")
    case _:
        print("Who?")
