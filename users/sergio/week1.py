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

#################################
# Base exercise
#################################
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



#################################
# Bonus 1
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



#################################
# Bonus 2
#################################
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

    @diameter.setter
    def diameter(self, diameter):

        self.__diameter = diameter
        self.__radius = diameter/2
        self.__area = pi*self.__radius**2


    @property
    def area(self):
        return self.__area

    def __str__(self):
        return f'radius: {self.radius}\ndiameter: {self.diameter}\narea: {self.area}'.format(self=self)

c=Circle()
print(c)
c.diameter=4
print(c)
c.area =4



#################################
# Bonus 3
#################################
class Circle:

    def __init__(self, radius=1):
        self.radius=radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")

        self.__radius = radius
        self.__diameter = 2*radius
        self.__area = pi*radius**2

    @property
    def diameter(self):
        return self.__diameter

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter/2


    @property
    def area(self):
        return self.__area

    def __str__(self):
        return f'radius: {self.radius}\ndiameter: {self.diameter}\narea: {self.area}'.format(self=self)

c=Circle()
print(c)
c.diameter=4
print(c)
c.area =4
c.radius=-1
c.diameter=-1