import random
from words import words 
import string
from hangman_visual import hangman_lives

def get_correct_word(words):
    word = random.choice(words)
    while "-" in word or " "in word:
        word = random.choice(words)
    return word.upper() #note:return upper case

def hangman():
    word = get_correct_word(words)
    required_letters = set(word) #letters in the word
    valid_letter = set(string.ascii_uppercase)
    used_letters = set() #guessed letters
    lives = 7 


    while len(required_letters) > 0 and lives > 0:
        # display letters already used
        print("You have", lives, "lives remaining and you used this letters: ", " ".join(used_letters))

        #display the word in eg (P - C K)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(hangman_lives[lives])
        print("Current word: ", " " .join(word_list))

        #player letter input
        player_letter = input("Input letter: ").upper()

        if player_letter in valid_letter - used_letters:
            used_letters.add(player_letter)
            if player_letter in required_letters:
                required_letters.remove(player_letter)
                print("")

            else:
                lives -= 1 #take away one life
                print("Letter",player_letter, "is not in the word")

         # in the case of player inputting a used letter       
        elif player_letter in used_letters:
            print("\nLetter already used. Try again.")

        else:
            print("\nInvalid character. Try again.")
        
    if lives == 0:
        print(hangman_lives[lives])
        print("Your lives got depleted. The word was", word)
    else:
        print("You got it right, the word was", word)
        


if __name__ == "__main__":
    hangman()


