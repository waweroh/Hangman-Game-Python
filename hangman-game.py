import random
from words import words 
import string

def get_correct_word(words):
    word =random.choice(words)
    # while '-' in word or ' ' in word:
    #     word = random.choice(words)
    return word

def hangman():
    word = get_correct_word(words)
    required_letters = set(word) #letters in the word
    valid_letter = set(string.ascii_uppercase)
    used_letters = set() #guessed letters

    while len(required_letters) > 0:
        #letters used
        print("You used this letters", " ".join(used_letters))
        #display the word in eg (P - C K)
        #word_list = [letter if letter in used_letters else "-" for letter in word]
        word_list = []
        for letter in word:
            if letter in used_letters:
                word_list.append(letter)
            else:
                word_list.append("-")
        print("Current word: ", " ".join(word_list))

        #player letter input
        player_letter = input("input letter: ").upper()
        if player_letter in valid_letter - used_letters:
            used_letters.add(player_letter)
            if player_letter in required_letters:
                required_letters.remove(player_letter)
                
        elif player_letter in used_letters:
            print("Letter already used. Try again.")

        else:
            print("Invalid character. Try again.")

# user_input = input("enter something:")
# print(user_input)
if __name__ == "__main__":
    hangman()













# def display_hangman(tries):
#     stages = [  # whole body
#                 """
#                    --------
#                    |      |
#                    |      O
#                    |     \|/
#                    |      |
#                    |     / \
#                    -
#                 """,
#                 # head, body, both arms, and one leg
#                 """
#                    --------
#                    |      |
#                    |      O
#                    |     \|/
#                    |      |
#                    |     / 
#                    -
#                 """,
#                 # head, body, and both arms
#                 """
#                    --------
#                    |      |
#                    |      O
#                    |     \|/
#                    |      |
#                    |      
#                    -
#                 """,
#                 # head, body, and one arm
#                 """
#                    --------
#                    |      |
#                    |      O
#                    |     \|
#                    |      |
#                    |     
#                    -
#                 """,
#                 # head and body
#                 """
#                    --------
#                    |      |
#                    |      O
#                    |      |
#                    |      |
#                    |     
#                    -
#                 """,
#                 # head
#                 """
#                    --------
#                    |      |
#                    |      O
#                    |    
#                    |      
#                    |     
#                    -
#                 """,
#                 # initial empty state
#                 """
#                    --------
#                    |      |
#                    |      
#                    |    
#                    |      
#                    |     
#                    -
#                 """
#     ]
#return stages[tries]