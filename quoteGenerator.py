#%%
from random_word import RandomWords
from quote import quote
import random

#Get random keyword to use for quote generation
r = RandomWords()

def get_valid_quote():
    while True:
        # Get a random word
        word = r.get_random_word()
        #print(f"Generated word: {word}")

        # Try to fetch a quote using the word
        result = quote(word)

        # If a quote is found, return it
        if result != None:
            #print(f"Found a quote for the word: {word}")
            return result

#Quote generation using keyword
result = get_valid_quote()

#Randomise the quote chosen for each keyword
i = random.randint(0, len(result)-1)
Quote = result[i]['quote']
Author = result[i]['author']
Book = result[i]['book']
print(f'''Quote:
{Quote} ~ {Author}, {Book}
      ''')