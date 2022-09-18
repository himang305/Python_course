import random

# 1. Generate two random single-digit integers
number1 = random.randint(0, 9)
number2 = random.randint(0, 9)

# 2. If number1 < number2, swap number1 with number2
if number1 < number2:
    number1, number2 = number2, number1 # Simultaneous assignment

# 3. Prompt the student to answer "What is number1 - number2?"
answer = eval(input("What is " + str(number1) + " - " + str(number2) + "? "))

# 4. Check the answer and display the result
if number1 - number2 == answer:
    print("You are correct!")
else:
    print("Your answer is wrong.\n", number1, '-', number2, "is", number1 - number2, '.')
    


from random import randint # import randint

# Generate a random character between ch1 and ch2
def getRandomCharacter(ch1, ch2):
    return chr(randint(ord(ch1), ord(ch2)))   # ord return value for a character - Unicode value

# Generate a random lowercase letter
def getRandomLowerCaseLetter():
    return getRandomCharacter('a', 'z')

# Generate a random uppercase letter
def getRandomUpperCaseLetter():
    return getRandomCharacter('A', 'Z')

# Generate a random digit character
def getRandomDigitCharacter():
    return getRandomCharacter('0', '9')

# Generate a random character
def getRandomASCIICharacter():
    return chr(randint(0, 127))