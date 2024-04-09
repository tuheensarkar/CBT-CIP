import random


def game():
    options = ['rock', 'paper', 'scissor']
    comp_choice = random.choice(options)
    user_choice = input("Enter your choice ")
    print("computer choice is", comp_choice)
    print("You'r choices", user_choice)
    if (comp_choice == user_choice.lower()):
        print("It's a tie")
    elif (comp_choice == 'rock') and (user_choice.lower() == 'paper') or (comp_choice == 'paper') and (
            user_choice.lower() == 'scissor') or (comp_choice == 'scissor') and (user_choice.lower() == 'rock'):
        print("You win!")
    else:
        print("Computer win!")
    play_again = input("Do you want to play again? (yes/no) ")

    if play_again == 'yes':
        game()

    else:
        print("Thank you")
game()
