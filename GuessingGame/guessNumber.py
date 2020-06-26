from General_Functions.colorPrint import colorPrint, colorString, Colors
import random

MIN = 1
MAX = 10
GUESSES = 3

STRING_RANGE = colorString(MIN, Colors.LIGHT_BLUE) + " and " + colorString(MAX, Colors.LIGHT_BLUE)


def getUserInput(userPrompt):
    try:
        userInput = input(userPrompt)
    except EOFError:
        userInput = None
    return userInput


playing = True

print("I will come up with a number between", STRING_RANGE)
print("It's your job to guess it! You have", colorString(GUESSES, Colors.RED), "guesses!")
while playing:
    guessesLeft = GUESSES
    won = False
    randomNum = random.randint(MIN, MAX)
    while guessesLeft > 0:
        guess = getUserInput("What is your guess? ")
        if guess is None:
            playing = False
            break
        if guess.isdigit() and MIN <= int(guess) <= MAX:
            if int(guess) == randomNum:
                won = True
                break
            else:
                print("Sorry, that's", colorString("WRONG", Colors.RED))
            guessesLeft = guessesLeft - 1
        else:
            print("That's an invalid guess! Guess a number between", STRING_RANGE)
    if playing:
        if won:
            colorPrint("You're right! Congratulations!", Colors.PINK)
        else:
            colorPrint("Dun dun dun... You lost!", Colors.BLUE)
        print("The actual number was", colorString(randomNum, Colors.RED))
        again = getUserInput("Do you want to play again? Type 'Y' to play again! ")
        if again is None or again.lower() != 'y':
            playing = False
print("Thanks for playing!")

