# Day 11 Exercise
# Bradley Brosovich

"""
In the same folder of your D16Files.py, create a data.txt with the content below:

Robert, Jones, 2015
Michael, Taylor, 2010
William, Brown, 2037
David, Williams, 2033
James, Wilson, 2048
Paul, Lewis, 2037
"""

def read_file():
    """
    01. read a file
    Finish this function which reads the content of the data.txt and print the content line by line.
    This function has no explicit return value.
    """
    fileRef=open("data.txt","r")
    for line in fileRef:
        print(line)
    fileRef.close()
def read_file_definite():
    """
    02. read a file with a definite loop
    Finish this function which reads the FIRST 3 LINES of the data.txt and print them out.
    This function has no explicit return value.
    """
    fileRef = open("data.txt", "r")
    i=0
    for line in fileRef:
        print(line)
        i+=1
        if i >2:
            break
    fileRef.close()

def read_file_indefinite():
    """
    03. read a file with an indefinite loop
    Finish this function which reads the data.txt file, then process each line as CSV.
    It prints all the first names of each line.
    But the printing stops after printing the first occurrence of first name has 7 characters.
    This function has no explicit return value.
    """
    fileRef = open("data.txt", "r")
    line = fileRef.readline()
    j=0
    while line:
        values = line.split(',')
        print(values[0])
        line = fileRef.readline()
        if len(values[j]) == 7:
            break
        j+=1
    fileRef.close()
def write_file():
    """
    04. write a file
    Finish this function which reads the data.txt file , read the content line by line.
    For each line it reads, it should also output one line in a out.txt file with the content below
    {first name} {last name}'s office is {office}.

    For example, after reading the first line, the line added to the out.txt should be
    "Robert Jones's office is  2015".
    This function has no explicit return value.
    """
    fileRef = open("data.txt", "r")
    fileOut = open("names.txt","w")
    line=fileRef.readline()
    while line:
        listV= line.split(",")
        fileOut.write(listV[0]+" "+listV[1]+"'s "+"office is"+listV[2])
        line=fileRef.readline()

    fileRef.close()
    fileOut.close()


#=======================================
# test for Q1
read_file()
print("--"*10)

#test for Q2
read_file_definite()
print("--"*10)

#test for Q3
read_file_indefinite()
print("--"*10)

#test for Q4
write_file()

