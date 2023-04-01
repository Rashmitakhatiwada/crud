from create import create
from read import read
from update import update
from delete import delete

def inquiry():
    selection = input("welcome to broadway. please select C/R/U/D/E ")
    selection = selection.lower()

    def continue_or_not(c):
        inquiry() if c else print("thank you. see you again")

    if selection == "c":
        cont = create()
        return continue_or_not(cont)
        # if cont:
        #     inquiry()
        # else:
        #     print("thank you. see you again")

    elif selection == "r":
        id = input("enter the id of a student")
        cont = read(id)
        return continue_or_not(cont)

    elif selection == "u":
        id = input("enter the id of a student")
        to_change = input("what do you wish to update? id, name or department")
        value = input(f"give the new {to_change}")
        cont = update(id, to_change, value)
        return continue_or_not(cont)

    elif selection == "d":
        id = input("enter the id of a student you want to delete")
        cont = delete(id)
        return continue_or_not(cont)

    else:
        print("thank you. see you again")

if __name__ == "__main__":
    inquiry()
