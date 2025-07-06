#  Make a guessing game --> 
from random import randint

guessTime= int(input("Enter a count number how many time you run guess number  : "))

won =[]
lost =[]

for x in range(1,guessTime+1):
    guessNum= int(input("Enter Your Guess Number between 1 to 5: "))

    randomNum = randint(1,5)

    if guessNum == randomNum :
        print("You guessed correct number")
        won.append(x)
    else :
        print(f"You guessed worng number, The Correct number is {randomNum}")
        lost.append(x)
        
print(f"Won = {len(won)}-->{won}, \n Lost = {len(lost)}-->{lost}")