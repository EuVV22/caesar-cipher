# add your code here
def _main_():
    # Ask user for input
    print("Please enter a senctence: ")
    message = str(input())
    cipher = ""

    # Loop throw each character of the string
    for character in message:
        # check if character is a letter
        if character.isalpha():
            # Change position
            new_character = new_letter(character)
        else:
            new_character = character
        # add to result string
        cipher += new_character
    
    # print(f"The encrypted sentence is: {cipher}")
    print(cipher)

def new_letter(letter: str) -> str:
    # Define consts
    NUMBER_OF_MOVEMENTS = 5
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
    QUANTITY_OF_LETTERS = ALPHABET.__len__()

    position = ALPHABET.index(letter.lower())
    
    new_position = position + NUMBER_OF_MOVEMENTS
    
    if new_position > 25:
        new_position -= QUANTITY_OF_LETTERS
    
    return ALPHABET[new_position]

_main_()