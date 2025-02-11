def yes_no(question):
    """checks that users enter a yes/y and a no/n"""

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Sorry, this is a yes(y) and no(n) question. Please answer with the 2 options.\n")

# main routine starts here.


# loop for testing purposes
while True:
    want_instructions = yes_no("Do you want to read the instructions?")
    print(f"you chose {want_instructions}\n")
