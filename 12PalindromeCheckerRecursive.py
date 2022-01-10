# Day 12 Exercise  (PA6)

"""
Part 2:
Write a recursive method that checks whether a string is a palindrome.
Specifically, your method should be called check_palindrome.
This function should return a True if the parameter is a palindrome string, return a False otherwise.
If the submitted solution is not recursive, then this problem will receive a zero.
"""
def check_palindrome(a_string):
    if len(a_string) <= 1:
        return True
    else:
        if a_string[0] == a_string[-1]:
            return check_palindrome(a_string[1:-1])
        elif a_string[0] != a_string[-1]:
            return False

### Code to test your work, do not change:
print(check_palindrome("aaaa"))
print(check_palindrome("aaa"))
print(check_palindrome("abba"))
print(check_palindrome("aba"))
print(check_palindrome("abcba"))

print(check_palindrome("abca"))
print(check_palindrome("abdsa"))
### Expected output:
#True
#True
#True
#True
#True
#False
#False

