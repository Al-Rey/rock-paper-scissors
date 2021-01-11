"""
Author: Al-Rey
Date: 1/11/2021
Desc: A simple rock paper scissors game with the user playing against an AI
"""


import random as rand

# Constants
CHOICES = ["rock", "paper", "scissors"]
AI_WINS = "The AI wins!"
PLAYER_WIN = "You Win!"

# the AI class
class AI:
    def __init__(self):
        self.choice = ""

    # picks the choice for the AI
    def pick(self):
        rand.seed()
        num = rand.randint(0, 2)

        self.choice = CHOICES[num]

    # returns the choice of the AI
    def getChoice(self):
        return self.choice


# determines who wins
def winner(player_choice, AI_choice):
    if player_choice == AI_choice:
        print("It's a tie!")
    elif player_choice == CHOICES[0]:   # player picks rock
        if AI_choice == CHOICES[1]:     # AI picks paper
            print(AI_WINS)
        else:   #AI picks scissors
            print(PLAYER_WIN)
    elif player_choice == CHOICES[1]:   # player picks paper
        if AI_choice == CHOICES[0]: # AI picks rock
            print(PLAYER_WIN)
        else:   # AI picks scissors
            print(AI_WINS)
    else:   # the player picks scissors
        if AI_choice == CHOICES[0]: # AI picks rock
            print(AI_WINS)
        else: # AI picks paper  
            print(PLAYER_WIN)


# gets the player's choice of rock, paper, or scissors
def get_player_input():
    choice = ""
    while choice.lower() not in CHOICES:
        choice = input("Do you pick rock, paper, or scissors?")
    
    return choice.lower()


# the main function that plays the game
def play_game():
    play_again = True

    # loops on until the player doesn't want to play again
    while play_again:
        opponent = AI()
        
        # get the choices for the player and the AI
        player = get_player_input()
        opponent.pick()

        print("")

        # display what each of their choices are
        print("Player: ", player)
        print("AI: ", opponent.getChoice())

        winner(player, opponent.getChoice())

        # check if the player wants to play again
        answer = ""

        while answer.lower() != "yes" and answer.lower() != "no":
            answer = input("would you like to play again (yes/no)")

        if answer.lower() == "no":
            play_again = False 

        print("")

    # ending message when the player is done playing
    print("Thanks for playing!")


# Unit Testing
# basically testing some parts of the program
def unit_testing():
    # test if the AI picking works
    testAI = AI()
    for i in range(1, 10):
        testAI.pick()
        print(testAI.getChoice())

    # get player input
    print(get_player_input()) 


if __name__ == "__main__":
    play_game()

