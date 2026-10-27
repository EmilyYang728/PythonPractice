import  random

number = random.randint(1,100)

guess = 1 # create variable guess

print("a random number is chosen, try guessing it")


def check_answer():

    tries = 1

    guess = int(input("number from 1-100? "))

    while guess != number:

        tries += 1
                
        if guess < number:
            print("too low")
        elif guess > number:
            print("too high")

        guess = int(input("another guess? "))

    return tries
        
tries = check_answer()

print("yay u got it")
print("correct answer is: " , number)
print("you took " , tries , " tries")
