def int_check(question, low, high):
    """Checks users enter an integer / float that is more than zero"""

    error = f"Please enter a number between {low} and {high}"

    while True:

        try:
            # change response to be an integer and make sure it is higher than Zero.
            response = int(input(question))

            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# main routine goes here
while True:
    print()

    my_int = int_check("Choose a number: ", 1, 10)
    print(f"Thanks, You Chose {my_int}")
