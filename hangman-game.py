import random
from words import words 
import string

def get_correct_word(words):
    word = random.choice(words)
    while "-" in word or " "in word:
        word = random.choice(words)
    return word

def hangman():
    word = get_correct_word(words)
    required_letters = set(word) #letters in the word
    valid_letter = set(string.ascii_uppercase)
    used_letters = set() #guessed letters

    while len(required_letters) > 0:
        # display letters already used
        print("You used this letters: ", " ".join(used_letters))
        #display the word in eg (P - C K)
        word_list = []
        for letter in word:
            if letter in used_letters:
                word_list.append( letter)
            else:
                word_list.append("-")
        print("Current word: ", " ".join(word_list))

        #player letter input
        player_letter = input("Input letter: ").upper()
        
        if player_letter in valid_letter - used_letters:
            used_letters.add(player_letter)
            if player_letter in required_letters:
                required_letters.remove(player_letter)

         # in the case of player inputting a used letter       
        elif player_letter in used_letters:
            print("Letter already used. Try again.")

        else:
            print("Invalid character. Try again.")
        
        if len(required_letters) == 0:
            print("You win! The word was", word)
            break


if __name__ == "__main__":
    hangman()


