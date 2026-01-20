#LOOP
# Ask : roll the dice
#if user enters yes 
#  generrate two random numbers
# print them 
#if user enters n 
#print thanks you massage
#terminate
#Else 
#  print invalid choice



import random


while True:
    ask = input("Roll the dice? (Y/N):").upper()


    a = random.randint(1, 10)
    b = random.randint(10,20)

    if (ask == "YES"):
        print(f"({a}, {b})")

    elif (ask == "NO"):
        print("Thanks for playing")
        break

else:
    print("Invalid choice")
