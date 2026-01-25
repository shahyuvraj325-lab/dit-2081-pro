import random

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0
    rounds = 3  # Play 3 rounds
    
    print("Welcome to Rock-Paper-Scissors!")
    print("Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock.")
    print(f"We'll play {rounds} rounds. Best of luck!\n")
    
    for round_num in range(1, rounds + 1):
        print(f"Round {round_num}:")
        user_choice = input("Choose rock, paper, or scissors: ").lower().strip()
        
        if user_choice not in choices:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue
        
        computer_choice = random.choice(choices)
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1
        
        print(f"Score: You {user_score} - Computer {computer_score}\n")
    
    print("Game Over!")
    if user_score > computer_score:
        print("You won the game!")
    elif user_score < computer_score:
        print("Computer won the game!")
    else:
        print("It's a tie game!")

# Run the game
rock_paper_scissors()