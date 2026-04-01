'''Write a recursive function to count occurrences of a character in a string'''

string1=input("Enter a string: ")
target=input("Enter a character whose occurance is to be counted: ")

def count_char(string1,target):
    if string1=="":
        return 0
    else:
        if target==string1[0]:
            return 1 + count_char(string1[1:],target)
        else:
            return count_char(string1[1:],target)
print(count_char(string1,target))