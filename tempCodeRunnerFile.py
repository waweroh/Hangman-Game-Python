def display_hangman(tries):
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
#     return stages[tries]