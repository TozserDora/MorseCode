import requests
from unidecode import unidecode

ENDPOINT = "https://api.funtranslations.com/translate/morse.json"

while True:
    user_input = input("What shall I translate into Morse code? (Type 'exit' to exit.) ")
    text_without_accents = unidecode(user_input)

    if user_input == 'exit':
        break

    # This is the Public API (max 5 calls/hour and 60 calls/day). For more, an API key is needed.
    params = {"text": text_without_accents}
    response = requests.get(url=ENDPOINT, params=params)

    if response.ok:
        code = response.json()
        try:
            print(response["contents"]["translated"])
        except KeyError:
            print("Sorry, that contains an invalid character!")
    else:
        print("Sorry, the API request was denied. Try again later!")
        break