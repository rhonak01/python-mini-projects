import random


com = random.randint(1, 100)#number that gussed by computer

while True:
    try:
        num= int(input("guess a number between(1/100) :"))
   


        if (num > 100):
            print("invaid input!")
            break

        elif (num > com):
            print("too high!")

        elif(num < com):
            print("too low!")

        elif (num == com):
            print("congratulation! You guessed the number .")
            break
    except ValueError:
        print("Please enter a valid number")
  