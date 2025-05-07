import random
print("welcome to 3bwahab number guess game. \n you got 7 chance to guess the correct number . have a good luck ")
guessingNumber=random.randrange(100)
limit=7
chance=0
while chance<limit:
    chance+=1
    number=int(input("Enter Your Guess: "))

    if number ==guessingNumber:
        print(f'congratulations you found the right number {guessingNumber} in the {chance} attempt')
        break
    elif chance>=limit and number!=guessingNumber:
        print(f'Oops sorry, the number is {guessingNumber} better luck in the next time ')
    elif number >guessingNumber:
        print("your guess is higher")
    elif number < guessingNumber:
        print("your guess is lesser")