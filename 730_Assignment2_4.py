'''Write a Python program to iterate through a string and count the number of vowels present in it.'''
string1=input("Enter a string: ")
count=0
for i in string1:
    if i in "aeiou":
        count+=1
print("The total number of vowels in the given string is: ",count)
