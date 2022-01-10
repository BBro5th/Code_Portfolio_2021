# Day 1 Exercise

def do_math():
    """
    Create code within this function definition to do calculations below:
    What is 2 + 2?
    What is 10 / 3?
    What if I want integer division of 10 / 3?
    How do I compute 2 powers 10? (should be 1024)
    Write code to show your answers of those questions.
    There is no return value for this function.
    """
    mydeth= 2+2
    mylyfe= 10/3
    mynife=10//3
    mykite=2**10
    print(mydeth,mylyfe,mynife,mykite)

def do_strings():
    """
    Create my_string variable with value "casablanca"
    There is no return value for this function.
    Find the length of the string
    What is the 4th character?
    Print the substring of length 3 that starts at index 1.
    Is “cat” inside of your string?
    Does your string start with “a”?
    Write code to show your answers of those questions.
    There is no return value for this function.
    """
    Cas="casablanca"
    print(len(Cas))
    print(Cas[3])
    print("cat" in Cas)
    print(Cas.startswith("a"))

def more_about_yourself():
    """
    Use print statements to tell your instructor more about yourself:
    When did you take CSC131?
    Based on your experience in CSC131 (or other intro-level programing courses), what helped you the most in
    learning programing?
    How do you plan to back up your programs for this course?
    """
    print("i took CSC131 during last summer semester")
    print("physically doing the code and when i helped others i saw the many different approaches that they took")
    print("I plan on using microsoft one drive, or a similar online method")

#######################################
# callers, do not change the code below
#######################################
do_math()
print("--"*10)
do_strings()
print("--"*10)
more_about_yourself()
print("--"*10)

