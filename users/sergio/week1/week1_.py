import math

# Base
class Circle:

    def __init__(self, radius=1):
        self.radius = radius
        self.diameter = 2*radius
        self.area = math.pi * radius**2

    def __repr__(self):
        return(f'Circle({str(self.radius)})')

c = Circle()
c.radius
c.diameter
c.area
print(c)

# Bonus 1
class Circle:

    def __init__(self, radius=1):
        self.radius = radius

    def __repr__(self):
        return(f'Circle({str(self.radius)})')

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def area(self):
        return math.pi * self.radius **2

c = Circle()
c.radius
c.diameter
c.area
c.radius = 2
c.diameter
c.area


# Bonus2
class Circle:

    def __init__(self, radius=1):
        self.radius = radius

    def __repr__(self):
        return (f'Circle({str(self.radius)})')


    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2

    @property
    def area(self):
        return math.pi * self.radius ** 2

c = Circle()
c.diameter = 4
c.radius
c.area



# Bonus3
class Circle:

    def __init__(self, radius=1):
        self.radius = radius

    def __repr__(self):
        return (f'Circle({str(self.radius)})')


    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        if radius < 0:
            raise ValueError('Negative radio is not possbile')
        self._radius = radius


    @property
    def area(self):
        return math.pi * self.radius ** 2

c = Circle()
c.radius = 4
c.diameter
c.area

c.diameter = -3
c.radius = -2