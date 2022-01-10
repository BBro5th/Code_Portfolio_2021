# Day 11 Exercise

"""
Write two recursive functions to counts the vowels (upper and lower cases) in a given string as argument.
Specifically, your functions should be called count_vowels1(some_str) and count_vowels(some_str).

count_vowels1(some_str):
Base cases: should consider the some_string has 1 or 0 character
Recursive step: count(some_str) = count(str_left) + count(str_right), given the some_str has more than 2 characters

count_vowels2(some_str)
Base cases: should consider the some_string has 1 or 0 character
Recursive step:
count(some_str) = 1+ count(remaining_str)  if the first character is a vowel
count(some_str) = 0+ count(remaining_str)  if the first character is not a vowel

You cannot use iterations, or built-in method count() in your solution.
Both functions should return an integer as the number of vowels in the string.
"""

def count_vowels1(some_str):
    if len(some_str) == 1:
        if some_str[0] in "aeiouAEIOU":
            return 1
        else:
            return 0
    elif len(some_str) == 0:
        return 0
    else:
        return count_vowels1(some_str[0:((len(some_str))//2)]) + count_vowels1(some_str[((len(some_str))//2):])


print(count_vowels1(""))  # 0
print(count_vowels1("hello world"))  # 3
print(count_vowels1("231 is becoming harder and harder =("))  # 9
print(count_vowels1("but I can pass!"))  # 4
print("---"*10)

def count_vowels2(some_str):
    if len(some_str) is 1:
        if some_str[0] in "aeiouAEIOU":
            return 1
        else:
            return 0
    elif len(some_str) is 0:
        return 0
    else:
        return count_vowels2(some_str[1:]) + count_vowels2(some_str[0])

print(count_vowels2(""))  # 0
print(count_vowels2("hello world"))  # 3
print(count_vowels2("231 is becoming harder and harder =("))  # 9
print(count_vowels2("but I can pass!"))  # 4
print("---"*10)