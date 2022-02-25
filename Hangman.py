import random
import string
from words import words

def get_valid_word(words):
    word= random.choice(words) # get a random words from word list (word.py)
    while '-' in word or ' ' in word:
         word= random.choice(words)
          
    return word.upper()

def hangman():
    word= get_valid_word(words)
    word_letters= set(word) #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters= set() # what user has guessed
    
    while len(word_letters) > 0:
        #letters user
        # " ".join(['a', 'b','cd']) -> 'a b cd'
        print("You have used these letters: ", " ".join(used_letters))
        
        # what current word is (i.e W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter= input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
        
        elif user_letter in used_letters:
            print("You have already used this character. please try again.")

        else:
            print("Invalid character. Please try again!")

        print('Yay! You guessed the word', word, '!')
if __name__ == '__main__':
    hangman()