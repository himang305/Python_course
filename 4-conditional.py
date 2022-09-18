x = 10
y = 20

print(x == y)

z = (x != y)
print(type(z))
m = (x < y)
print(m)
print(x >= y)
print(x <= y)

if x == y:
    print('x IS equal to y')
else:
    print("X is NOT equal to y")

grade = 80
letterGrade = 'A'
if grade < 60:
    letterGrade = 'F'
elif grade >= 60 and grade < 70:
    letterGrade = 'D'
elif grade >= 70 and grade < 80:
    letterGrade = 'C'
elif grade >=80 and grade < 90:
    letterGrade = 'B'
else:
    letterGrade = 'A'

print(letterGrade)

year = eval(input("Enter a year: "))
zodiacYear = year % 12
if zodiacYear == 0:
    print("monkey")
elif zodiacYear == 1:
    print("rooster")
elif zodiacYear == 2:
    print("dog")
elif zodiacYear == 3:
    print("pig")
elif zodiacYear == 4:
    print("rat")
elif zodiacYear == 5:
    print("ox")
elif zodiacYear == 6:
    print("tiger")
elif zodiacYear == 7:
    print("rabbit")
elif zodiacYear == 8:
    print("dragon")
elif zodiacYear == 9:
    print("snake")
elif zodiacYear == 10:
    print("horse")
else:
    print("sheep")
    










