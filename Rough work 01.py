'''def op(n1 ,b_op ,n2):
    if basic_op=="add":
        print(num1,'+',num2,'=',num1+num2 )
num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))
basic_op=input("Enter the operation you want to perform: ")
op(num1 ,basic_op ,num2)

#  ERROR------>  print('Don't worry')
print('Don\'t worry')  #Correct way
print("HEY\tThere")
print("Hello\nEveryone")

number = 5
total = 0

while number != 0:
   total = total + number    # Infinite loop
   number = number + 1
   print(number)'''

import random

def get_user_choice():
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please enter rock, paper, or scissors.")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = random.choice(["rock", "paper", "scissors"])

        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        print(f"Your score: {user_score}")
        print(f"Computer's score: {computer_score}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

if __name__ == "__main__":
    play_game()














