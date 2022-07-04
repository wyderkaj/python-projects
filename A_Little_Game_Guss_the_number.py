import random
import time

print("Guess the number!\n")
time.sleep(1)
print("Hi! Welcome to the guessing game. I am going to pick a number between 1 and 100."
      "\nYour task is to guess that number.")
time.sleep(0.5)
answer= input("Do you want to play? Enter 'Yes' or 'No': ")
time.sleep(0.5)

while answer.lower() != "no":
    print("Picking a number...")
    time.sleep(3)
    print("I pick a number.")
    time.sleep(1)

    guess = int(input("What is your guess!: "))
    correct_number = random.randint(1,100)
    guess_count = 1

    while guess != correct_number:
        time.sleep(1)
        guess_count += 1
        if guess < correct_number:
            guess = int(input("Wrong. You need to guess higher. \nWhat is your guess!: "))
        else:
            guess = int(input("Wrong. You need to guess lower. \nWhat is your guess!: "))
        
    print(f"Congrats! The right answer was {correct_number}. It took you {guess_count} guesses.")
    
    answer= input("Do you want to play again? Enter 'Yes' or 'No': ")          
print("Goodbye!") 
