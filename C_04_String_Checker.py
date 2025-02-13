def string_checker(question, valid_ans_list):
    '''Checks that users enter the full word or the first letter of a word from a list of valid responses.'''

    while True:

        response = input(question).lower()

        for item in valid_ans_list:

            # check if the response is the entire word
            if response == item:
                return item

            # check if it's the first letter.
            elif response == item[0]:
                return item

        print(f"please choose an option from {valid_ans_list}")


# main routine goes here
levels = ['easy', 'medium', 'hard']

like_coffee = string_checker("Do you like coffee? ", ['yes', 'no'])
print(f"you chose {like_coffee}")
choose_level = string_checker("choose a level:", levels)
print(f"you chose {choose_level}")
