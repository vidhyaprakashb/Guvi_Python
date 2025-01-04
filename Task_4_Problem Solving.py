# Task 1: This program defines a class Circle with a constructor that takes a list as an argument.
class Circle:
    def __init__(self, radii_list):
        self.radii = radii_list  # Store the list of radii as an instance variable

radii_list = [10, 501, 22, 37, 100, 999, 87, 351]
circle = Circle(radii_list)
print("Radii List:", circle.radii)



# Task 2: This program demonstrates a class with a private variable pi = 3.141.
class Circle:
    __pi = 3.141  # Private class variable for the value of pi

    def get_pi(self): # Method to retrieve the value of the private variable __pi.
        return self.__pi

circle = Circle()
print("Value of Pi:", circle.get_pi())



# Task 3:  This program includes methods to calculate the area and perimeter for a list of radii.
class Circle:
    __pi = 3.141  # Private class variable for the value of pi

    def __init__(self, radii_list): #Constructor to initialize the Circle class with a list of radii.

        self.radii = radii_list  # Store the list of radii as an instance variable

    def Area(self): #Calculates the area for each radius in the list.
                    #Formula: Area = pi * r^2
        return [round(self.__pi * r**2, 2) for r in self.radii]

    def Perimeter(self):# Calculates the perimeter for each radius in the list.
                        # Formula: Perimeter = 2 * pi * r
        return [round(2 * self.__pi * r, 2) for r in self.radii]

radii_list = [10, 501, 22, 37, 100, 999, 87, 351]
circle = Circle(radii_list)
print("Areas:", circle.Area())
print("Perimeters:", circle.Perimeter())