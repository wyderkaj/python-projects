
import random
from words import words
from hangman_visual import lives_visual_dict
import string

print("Welcome to hangman game!\n")
print("Try to guess the word by specifying one letter at a time. You have 9 lives.\n")
print("Good Luck!\n")

def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or ' ' in word:  
        word = random.choice(words)   #when it stops iterating, we'll get a word that doesn't have a space or dash in it
        
    return word.upper() 


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word, the way of keeping track of what's already been guessed in the word
    alphabet = set(string.ascii_uppercase) #alphabet. import list of uppercase characters in the English dictionary
    used_letters = set()  # empty set, which is used in order to keep track of what the user has guessed.

    lives = 9

    # getting user input
    while len(word_letters) > 0 and lives > 0:  
        # letters they've already used
        # ' '.join(['a', 'b', 'cd']) turns this list into a string, sapareted by a space --> 'a b cd'
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))    

        # what current word is with dashes where the character that they havent't guessed are (ie W - R D) 
        word_list = [letter if letter in used_letters else '-' for letter in word]  
        print(lives_visual_dict[lives]) 
        print('Current word: ', ' '.join(word_list))    #create a string using that list

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:  #if this a valid character in the alphabet that I haven't used yet
            used_letters.add(user_letter)   #add this to used letter set. 
            if user_letter in word_letters:     #if the letter that I just guessed is in the word
                word_letters.remove(user_letter)    #remove that letter from word letters 
                print('')

            else:
                lives = lives - 1  # takes away a life if wrong
                print('\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:   
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nThat is not a valid letter.')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(lives_visual_dict[lives])
        print('You died, sorry. The word was', word)
    else:
        print('YAY! You guessed the word', word, '!!')


if __name__ == '__main__':
    hangman()
    