import re

def is_palindrome(phrase):
    forwards = ''.join(re.findall(r'[a-z]+', phrase.lower()))
    backwards = forwards[::-1]
    return forwards == backwards

if __name__ == '__main__':
    print("Python function that determines if a given string is a palindrome")
    string = input("Please. Enter your string: ")
    if is_palindrome(string) == True:
        print("It is a palindrome")
    else:
        print("It is not a palindrome")