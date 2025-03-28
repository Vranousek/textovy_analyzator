"""
projekt_1.py: první projekt do Engeto online Python Akademie

author: Daniel Vrána
email: deny.vrana@gmail.com
discord: vranousek
"""

TEXTS = [
    """
    Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30N and the Union Pacific Railroad,
    which traverse the valley.
    """,
    """
    At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.
    """,
    """
    The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.
    """
]

users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

username = input("Username: ")
password = input("Password: ")

if username in users and users[username] == password:
    print("-" * 40)
    print(f"Welcome to the app, {username}")
    print("We have 3 texts to be analyzed.")
    print("-" * 40)

    text_number = input("Enter a number btw. 1 and 3 to select: ")
    if text_number.isdigit():
        text_number = int(text_number)
        if text_number in [1, 2, 3]:
            selected_text = TEXTS[text_number - 1]
            words = selected_text.split()

            word_count = 0
            titlecase_words = 0
            uppercase_words = 0
            lowercase_words = 0
            numeric_strings = []
            word_lengths = {}
            sum_numbers = 0

            for word in words:
                clean_word = word.strip(".,!?")
                word_length = len(clean_word)
                if word_length > 0:
                    word_count += 1
                    if clean_word.istitle():
                        titlecase_words += 1
                    if clean_word.isupper():
                        uppercase_words += 1
                    if clean_word.islower():
                        lowercase_words += 1
                    if clean_word.isdigit():
                        numeric_strings.append(int(clean_word))
                        sum_numbers += int(clean_word)
                    if word_length in word_lengths:
                        word_lengths[word_length] += 1
                    else:
                        word_lengths[word_length] = 1

            print("-" * 40)
            print(f"There are {word_count} words in the selected text.")
            print(f"There are {titlecase_words} titlecase words.")
            print(f"There are {uppercase_words} uppercase words.")
            print(f"There are {lowercase_words} lowercase words.")
            print(f"There are {len(numeric_strings)} numeric strings.")
            print(f"The sum of all the numbers {sum_numbers}")
            print("-" * 40)

            print("LEN|  OCCURRENCES  |NR.")
            print("-" * 20)
            for length, count in sorted(word_lengths.items()):
                print(f"{length:3} | {'*' * count:<13} |{count}")
        else:
            print("Invalid selection, terminating the program..")
    else:
        print("Invalid input, terminating the program..")
else:
    print("Unregistered user, terminating the program..")
