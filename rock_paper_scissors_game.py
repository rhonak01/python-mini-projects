import random
choices = ["r","p","s"]
emojis = {'r':"🪨","p":"📰","s":"✂️"}

def get_user_choice():
    while True:
        user = input("rock, paper, or scissors ? (r/p/s) :").lower()
        if user in choices:
            return user    
        else:
            print("Invalid choice!") 

def display_choices(user_choice, computer):
    print(f"you chose {emojis[user_choice]}")
    print(f"computer chose {emojis[computer]}") 

def determine_winner(user_choice, computer):
    if user_choice == computer:
        print("tie!")

    elif (
        (user_choice == "r" and computer == "s") or 
        (user_choice == "s" and computer == "p") or 
        (user_choice == "p" and computer == "r")):
        print("You win"  )
        
    else:
        print("You lose")        
def play_game():
    while True:
        user_choice = get_user_choice()

        computer = random.choice(choices)

        display_choices(user_choice, computer)

        

        determine_winner(user_choice, computer)

        ask = input("continue? (y/n): ").lower()
        if ask =="n":
            print("Thanks for playing")
            break
    

play_game()