from random import choice
from random import randint
from load_dictionary import load_file
import sys

"""A program which embeds a message in a list of surnames. The letters of
the message are hidden by alternating the hidden text between the
 second and third letter of a surname. The first name in the list isn't included
 and there are dummy surnames which do not contain any hidden letters
 
 Example:
 
 first s(E)connd th(I)rd DUMMY f(O)urth fi(F)th DUMMY s(I)xth se(V)enth...
 
 would read E I O F I V
 
 INPUTS:
 hidden message = secret text to be concealed
 dummy_number = number of dummy words to be added
 
 OUTPUTS:
 list of surnames with a hidden message concealed within
 """
# ------------------------------------------------------------------------------
# INPUTS

# file containing second names
filename = 'names.txt'

# secret message
message = 'Give your word and we rise'

# number of dummy words
dummy_number = 3

# END OF INPUTS - DO NOT EDIT BELOW THIS LINE
# ------------------------------------------------------------------------------


def main():
    """Embed a hidden message in a list of surnames"""
    surnames = load_surnames('names.txt')
    prepped_message = prep_hidden_message(message)
    concealed_names = create_hidden_message(prepped_message, surnames)
    final_list = insert_dummy_names(concealed_names, dummy_number, surnames)
    # display the output
    print('List of households included in the survey: \n')
    print(*final_list, sep="\n")


def load_surnames(surnames_file):
    """Load in a text file of surnames and convert them into a list"""

    # Open, remove whitespace and convert to a list
    with open(surnames_file) as f:
        surnames = f.read().strip().split()

        return surnames


def create_hidden_message(prepped_message, surnames):
    """Conceal the message in a list of surnames"""
    list_items = []
    limit = len(prepped_message)

    for i in range(limit):

        if i == 0:
            # first item should not contain any letters of the hidden message
            list_items.append(choice(surnames))

        # For odd numbers the hidden message will be in the second position
        # of a given name
        elif i % 2 != 0:
            letter = prepped_message[i-1]

            for name in surnames:
                if letter.lower() == name[1] and name not in list_items:
                    list_items.append(name)
                    break

        # For even numbers the hidden message will be in third position
        else:
            letter = prepped_message[i-1]

            for name in surnames:
                if letter.lower() == name[2] and name not in list_items:
                    list_items.append(name)
                    break

    return list_items


def prep_hidden_message(hidden_message):
    """Change the messsage into one continuous string"""
    prepped = ''.join(hidden_message.split())

    return prepped


def insert_dummy_names(concealed_names, dummy_number, surnames):
    """Insert n number of dummy names somewhere into the concealed name list"""
    # Loop through the the number of dummy names chosen
    for i in range(dummy_number):

        # Keep trying names until an unused dummy name is found
        while True:
            # randomly select from the list
            dummy = choice(surnames)
            if dummy not in concealed_names:
                # randomly insert into the list
                insert_choice = randint(1, len(concealed_names))
                concealed_names.insert(insert_choice, dummy)
                break

            else:
                continue

    return concealed_names


if __name__ == '__main__':
    main()
