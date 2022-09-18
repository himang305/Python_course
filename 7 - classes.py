
# class: A class is a blueprint that defines the variables and the methods common to a set of objects.
# Instances are the concrete objects created from the class blueprint.


class Student:
    total_students = 0
    def __init__(self, first, last, email, phone):   # initializer of class  act as constructor
        self.first = first
        self.last = last
        self.email = email
        self.phone = phone
        Student.total_students += 1


    def printFullName(self):
        print(self.first + " " + self.last)

    def changePhone(self, newPhone):
        self.phone = newPhone



student1 = Student("John", "Doe", "john.doe@school.edu", 122354385)

# student1.first = 'John'
# student1.last = 'Doe'
# student1.email = 'john.doe@school.edu'
# student1.phone = 122354385


print(student1)
student2 = Student("Steve", "Fisherman", "steve.fisherman@school.edu", 489578948)

# student2 = Student()
# student2.first = 'Steve'
# student2.last = 'Fisherman'
# student2.email = 'steve.fisherman@school.edu'
# student2.phone =489578948

# print(student1.first + " " + student1.last)
# print(student2.first + " " + student2.last)

student1.printFullName()
student2.printFullName()

print(student2)

student1.changePhone(8080808080)
print(student1.phone)

print(Student.total_students)




# another class

import math

class Circle:
    def __init__(self, radius = 1):
        self.radius = radius

    def getPerimeter(self):
        return 2 * self.radius * math.pi

    def getArea(self):
        return self.radius * self.radius * math.pi

    def setRadius(self, radius):
        self.radius = radius



from Circle import Circle

def main():
    # Create a Circle object with radius 1
    myCircle = Circle()

    # Print areas for radius 1, 2, 3, 4 and 5
    n = 5
    printAreas(myCircle, n)

    # Display myCircle.radius and times
    print("\nRadius is", myCircle.radius)
    print("n is", n)

# Print a table of areas for radius
def printAreas(c, times):
    print("Radius \t\tArea")
    while times >= 1:
        print(c.radius, "\t\t", c.getArea())
        c.radius = c.radius + 1
        times = times - 1

main() # Call the main function        