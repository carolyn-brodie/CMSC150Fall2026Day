import math

class Circle:

    def __init__(self, radius):
        self.radius = radius


    def calculate_area(self):
        return math.pi * (self.radius ** 2)


    def __str__(self):
        return f"Circle with radius {self.radius}"



#(Aliasing) Using the Circle class on Moodle (with Sample Code for this week), do the following. Show the code and output for each step, and the answers to each question.
# Each step must be done OUTSIDE the Circle class, unless otherwise specified.
#(20 points)
# a.	Create a Circle object.                                                                         (1 point)
#
# b.	Create a second Circle object by assigning the first circle to it.                                                                                                     (1 point)
# c.	Write a method in the Circle class that makes a copy of a circle. The method should return a Circle object.                                                                                              (5 points)
# d.	Create a third circle object by making a copy (using your new method) of the first circle.                                           (1 point)
#
# e.	Print all 3 circles.          (1 point)
#
# f.	Write a method in the Circle class that stretches a circle by a given integer. E.g. if the integer is 3, the method should multiply the circle’s radius by 3.
#        The method must modify the Circle – NOT create a new circle.   In other words it should change the instance variable but not return anything.  This method should not have a
#        return statement, it should just change the radius attribute.   (5 points)
#
#
# g.	Modify the first circle  by stretching it by a factor of 2 (the integer passed in should be 2).                                                                                (1 point)
#
# h.	Print the first circle.                   (1 point)
#
# i.	Print the second circle. Was it changed? Explain why or why not.     (2 points)
#
# j.	Print the third circle. Was it changed? Explain why or why not.   (2 points)