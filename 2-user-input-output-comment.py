
# EVAL  - evaluate the statemnt to be valid python statement


#Prompt the user to enter a radius - taken as string 
radius = eval(input("Enter a value for radius: "))
# answer = eval(input("What is " + str(number1) + " - " + str(number2) + "? "))

# Compute area
area = radius * radius * 3.14159

# Display results
print("The area for the circle of radius", radius, "is", area)

import turtle

# Prompt the user for inputing two points
x1, y1 = eval(input("Enter x1 and y1 for point 1: "))
x2, y2 = eval(input("Enter x2 and y2 for point 2: "))

# Compute the distance
distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

# Display two points and the connecting line
turtle.penup()
turtle.goto(x1, y1) # Move to (x1 , y1)
turtle.pendown()
turtle.write("Point 1")
turtle.goto(x2, y2) # Draw a line to (x2, y2)
turtle.write("Point 2")

# Move to the center of the line
turtle.penup()
turtle.goto((x1 + x2) / 2, (y1 + y2) / 2)
turtle.write(distance)

turtle.done()

# extraline statement 
# if self.on and \
#                 1 <= self.volumeLevel <= 7:

stringss = """   # multiple line string
dfef
efwefgw"""

# Display the results
# print("Your amount", amount, "consists of\n",
#       "\t", numberOfOneDollars, "dollars\n",
#       "\t", numberOfQuarters, "quarters\n",
#       "\t", numberOfDimes, "dimes\n",
#       "\t", numberOfNickels, "nickels\n",
#       "\t", numberOfPennies, "pennies")

question2 = "Is your birthday in  Set2?\n" + \
            " 2 3 6 7\n" + \
            "10 11 14 15\n" + \
            "18 19 22 23\n" + \
            "26 27 30 31" + \
            "\nEnter 0 for No and 1 for Yes: "
            

print("          Multiplication Table")
# Display the number title
print("  |",end = '')
for j in range(1, 10):
    print("  ", j, end = '')
print() # Jump to the new line
print("----------------------------------------")

# Display table body
for i in range(1, 10):
    print(i, "|", end = '')
    for j in range(1, 10):
        # Display the product and align properly
        print(format(i * j, "4d"), end = '')
    print() # Jump to the new line            
