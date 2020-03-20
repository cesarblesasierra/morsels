# Hello!
#
# This week I want you to make a class that represents a circle.
# The circle should have a radius, a diameter, and an area. It should also have a nice string representation.
#
# For example:
#
# >>> c = Circle(5)
# >>> c
# Circle(5)
# >>> c.radius
# 5
# >>> c.diameter
# 10
# >>> c.area
# 78.53981633974483
# Additionally the radius should default to 1 if no radius is specified when you create your circle:
#
# >>> c = Circle()
# >>> c.radius
# 1
# >>> c.diameter
# 2
# There are three bonuses for this exercise.

# Base exercise

import numpy as np
from math import pi
class Circle:
    def __init__(self, radius=1):

        self.radius = radius
        self.diameter = 2*radius
        self.area = pi*radius**2

    def __str__(self):
        return f'radius: {self.radius}\ndiameter: {self.diameter}\narea: {self.area}'.format(self=self)


def base__battery_of_tests():

    c=Circle(5)
    assert c.radius == 5, 'Radius wrong'
    assert c.diameter == 10, 'Diameter wrong'
    np.testing.assert_approx_equal(c.area, 78.539, significant=3), 'Area wrong'
    print(c)

base__battery_of_tests()

# Bonus 1
# Base exercise
# Properties

#################################
# Using Property Function
class Circle:

    def __init__(self, radius=1):
        self.__set_radius(radius)

    def __set_radius(self, radius):
        self.__radius = radius
        self.__diameter = 2*radius
        self.__area = pi*radius**2

    def __get_radius(self):
        return self.__radius

    def __get_diameter(self):
        return self.__diameter

    def __get_area(self):
        return self.__area

    radius = property(fset=__set_radius, fget=__get_radius)
    diameter = property(fget=__get_diameter)
    area = property(fget=__get_area)

    def __str__(self):
        return f'radius: {self.__radius}\ndiameter: {self.__diameter}\narea: {self.__area}'.format(self=self)


def bonus1__battery_of_tests():
    c = Circle(2)
    c.radius = 1
    assert c.diameter == 2, 'Diameter is wrong'
    np.testing.assert_approx_equal(c.area, 3.141592653589793, significant=3)
    print(c)

bonus1__battery_of_tests()

# Using Decorator
class Circle:

    def __init__(self, radius=1):
        self.radius=radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        self.__radius = radius
        self.__diameter = 2*radius
        self.__area = pi*radius**2

    @property
    def diameter(self):
        return self.__diameter

    @property
    def area(self):
        return self.__area

    def __str__(self):
        return f'radius: {self.radius}\ndiameter: {self.diameter}\narea: {self.area}'.format(self=self)
def bonus1__battery_of_tests():
    c = Circle(2)
    c.radius = 1
    assert c.diameter == 2, 'Diameter is wrong'
    np.testing.assert_approx_equal(c.area, 3.141592653589793, significant=3)
    print(c)

bonus1__battery_of_tests()



## Bonus 2
c = Circle(2)
c.radius = 1
c.diameter
np.testing.assert_approx_equal(c.area, 3.141592653589793, significant=3)
print(c)







################################3
class Circle:

    def __init__(self, radius=1):
        self.__radius=radius
        self.__diameter = radius*2
        self.__area = pi*radius**2

    def __set_radius(self, radius):
        self.__radius = radius
        self.__diameter = 2*radius
        self.__area = pi*radius**2

    def __get_radius(self):
        return self.__radius

    def __set_diameter(self, diameter):
        self.__diameter = diameter
        self.__radius = diameter/2
        self.__area = pi*(diameter/2)**2

    def __get_diameter(self):
        return self.__diameter

    def __get_area(self):
        return self.__area

    radius = property(fset=__set_radius, fget=__get_radius, doc="My radius")
    diameter = property(fset=__set_diameter, fget=__get_diameter, doc="My diameter")
    area = property(fget=__get_area, doc="My area")

    def __str__(self):
        return f'radius: {self.__radius}\ndiameter: {self.__diameter}\narea: {self.__area}'.format(self=self)


def main():
    c=Circle(2)
    c.radius = 1
    assert c.radius == 1, 'Diameter is wrong'
    assert c.diameter == 2, 'Diameter is wrong'
    assert c.area == 3.14, 'Area is wrong'
    print('Test passed with success!!')

main()


# Bonus 2
# With decorators
# Properties
class Circle:

    def __init__(self, radius=1):
        self.__set_radius(radius)


    def __set_radius(self, radius):

        if radius < 0:
            raise ValueError("Radius cannot be negative")

        self.__radius = radius
        self.__diameter = 2*radius
        self.__area = pi*radius**2



    def __get_radius(self):
        return self.__radius

    def __set_diameter(self, diameter):
        self.__diameter = diameter
        self.__set_radius(diameter/2)
        self.__area = pi*(diameter/2)**2

    def __get_diameter(self):
        return self.__diameter

    def __get_area(self):
        return self.__area

    radius = property(fset=__set_radius, fget=__get_radius, doc="My radius")
    diameter = property(fset=__set_diameter, fget=__get_diameter, doc="My diameter")
    area = property(fget=__get_area, doc="My area")

    def __str__(self):
        return f'radius: {self.__radius}\ndiameter: {self.__diameter}\narea: {self.__area}'.format(self=self)

c=Circle(2)
c.radius = 1
c.diameter = -1
c.radius


def main():
    c=Circle(2)
    c.radius = 1
    assert c.radius == 1, 'Diameter is wrong'
    assert c.diameter == 2, 'Diameter is wrong'
    assert c.area == 3.14, 'Area is wrong'
    print('Test passed with success!!')

main()



# Con properties
class Circle:

    def __init__(self, radius=1):
        self.__radius = radius

    @property
    def __radius(self):
        return self.__radius

    @__radius.setter
    def __radius(self, radius):

        if radius < 0:
            raise ValueError("Radius cannot be negative")

        self.__radius = radius
        self.__diameter = 2*radius
        self.__area = pi*radius**2


    def __set_diameter(self, diameter):
        self.__diameter = diameter
        self.__set_radius(diameter/2)
        self.__area = pi*(diameter/2)**2

    def __get_diameter(self):
        return self.__diameter

    def __get_area(self):
        return self.__area

    radius = property(fset=__set_radius, fget=__get_radius, doc="My radius")
    diameter = property(fset=__set_diameter, fget=__get_diameter, doc="My diameter")
    area = property(fget=__get_area, doc="My area")

    def __str__(self):
        return f'radius: {self.__radius}\ndiameter: {self.__diameter}\narea: {self.__area}'.format(self=self)




def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

say_whee = my_decorator(say_whee)
say_whee
