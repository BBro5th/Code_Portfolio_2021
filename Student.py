# Day 5 Exercise

"""
Part 1: Defining a Student class
Rename this file to "Student.py" first.
Let's assume we need to store the student’s first name, last name and gpa.
Add a constructor that has three instance variables:
    - firstName
    - lastName
    - gpa
Create the __str__ method to print a student's information as:
<last name><SPACE><first name><SPACE><gpa>
"""
class Student:
    def __init__(self, first, last, gpa):
        self.firstname = first
        self.lastname = last
        self.gpa = gpa

    def __str__(self):
        return self.firstname + ", " + self.lastname + "\t" + str(self.gpa)
