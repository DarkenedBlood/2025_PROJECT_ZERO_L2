def string_checker(question, valid_ans_list, num_letters):
    '''Checks that users enter the full word or the first letter of a word from a list of valid responses.'''

    while True:

        response = input(question).lower()

        for item in valid_ans_list:

            # check if the response is the entire word
            if response == item:
                return item

            # check if it's the first letter.
            elif response == item[:num_letters]:
                return item

        print(f"please choose an option from {valid_ans_list}")


# main routine goes here
yes_no_list = ['yes', 'no']
coffee_list = ['cash', 'credit']

like_coffee = string_checker("Do you like coffee? ", yes_no_list, 1)
print(f"you chose {like_coffee}")
payment_type = string_checker("Payment method: ", coffee_list, 2)
print(f"you chose {payment_type}")
