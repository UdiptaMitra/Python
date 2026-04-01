'''Write a recursive function to check whether a string is a palindrome'''

string=input("Enter a string: ")
i=0
def is_palindrome(string,i=0):
    if i>=int(len(string)/2):
        return True
    if string[i]!=string[len(string)-1-i]:
        return False
    return is_palindrome(string, i+1)

if is_palindrome(string):
    print("Palindrome")
else:
    print("Not Palindrome")
