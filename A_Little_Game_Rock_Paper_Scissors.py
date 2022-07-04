from random import randint
import time

print("Game rock paper scissors!")
time.sleep(2)
print("You are about to play a game rock, paper, scissors against the computer.")
time.sleep(2)
print("You have to choose between rock, paper and scissors.")
time.sleep(2)
print("Rock crushes scissors, scissors cut paper, and paper covers rock. See who wins each round!")
time.sleep(2)

answer= input("Do you want to play? Enter 'Yes' or 'No': ")
time.sleep(0.5)
while answer.lower() != "no":
    tools = ["rock", "paper", "scissors"]
    #we have 3 options as an outcome, an option as a key, and a winner as a value
    results = {("paper", "scissors"): "scissors",
           ("paper", "rock"): "paper",
           ("rock", "scissors"): "rock"}

    user_choice = input("rock, paper or scissors: ")
    if user_choice not in tools:
         print("wrong answer.There is no such tool")
         continue

    comp_choice = tools[randint(0, 2)]
    print(comp_choice)
    if user_choice == comp_choice:
        print("Draft")
    else:
        for result in results:
            if user_choice in result and comp_choice in result:
                winner = results[result]
                if user_choice == winner:
                    print("You Win")
                else:
                    print("You Lose")
    time.sleep(1)
    answer= input("Do you want to play again? Enter 'Yes' or 'No': ")          
print("Goodbye!")                
        