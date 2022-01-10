# Day 5 Exercise
from Student import *

"""
Part 2: Create 2 student objects:
Yang Song with GPA 4.0
Garen Crownguard with GPA 2.5
Print out those two student objects.
"""
YangSong = Student("Yang","Song",4.0)
GarenCrownguard = Student("Garen","Crownguard",2.5)
print(YangSong)
print(GarenCrownguard)
print("--"*10)
"""
Part 3: Reading in students from a file  

I've created a file roster.txt that contains a list of students in the following format
<last name><SPACE><first name><SPACE><gpa>
In the Roster file, let's open up the roster.txt file and read in each line, then use the information of each line to create a student object.
Hint: to break up each line so that we can get the individual information, we can use split().
Hint: a GPA is supposed to be a float number
Once you've created a Student object, add it to a list of students.
When you've finished reading in the whole file, write another loop to print out each student.

Make a print statement to show the T(N) of your solution to part 3.
Make another print statement to show the Big O of your solution to part 3.
Hint: depending your program design, you may have a different T(n) to the T(n) on the solution. It is okay.
"""

Openroster = open("roster.txt","r")
Obekt= []
StudentList = []
Count = 0
MinDog = []
for line in Openroster:
    Obekt = line.split()
    StudLuck= Student(Obekt[0],Obekt[1],Obekt[2])
    print(StudLuck)
    StudentList.append(StudLuck)
    MinDog.append(Obekt[2])
    Count +=1
#print (Count) 100
Openroster.close()
print("T(n)= 6 + 6n")
print("T(N)= O(N)")

print("--"*10)
#print(StudentList[0])
THEGOSS=(min(MinDog))
Openroster = open("roster.txt","r")
OctoDad = []
for line in Openroster:
    OctoDad = line.split()
    StudLuck = Student(OctoDad[0], OctoDad[1], OctoDad[2])
    if OctoDad[2] == THEGOSS:
        print(StudLuck)

Openroster.close()
print("T(n) = 6 +6n + 3 + (4n)")
print("T(N) = O(N^2")
"""
Part 4: Do searches
Take the list of students and print the lowest GPA

Make a print statement to show the T(N) of your solution to part 4.
Make another print statement to show the Big O of your solution to part 4.
Hint: depending your program design, you may have a different T(n) to the T(n) on the solution. It is okay.
"""

