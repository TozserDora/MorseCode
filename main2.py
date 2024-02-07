from unidecode import unidecode
from morse import morse_dictionary

dictionary = morse_dictionary

while True:
    user_input = input("What shall I translate into Morse code? (Type 'exit' to exit.) ")
    text_polished = unidecode(user_input).lower()

    if user_input == 'exit':
        break

    code_list = []
    for letter in text_polished:
        try:
            morse_letter = dictionary[letter]
            code_list.append(morse_letter)
        except KeyError:
            print(f"Sorry, '{letter}' is an invalid character.")
            break

    code = " ".join(code_list)
    if len(code_list) == len(user_input):
        print(f"{user_input} with morse code: {code}")