'''Write a Python program to iterate through a dictionary and print all keys and their corresponding values'''
dict={}
n=int(input("Enter total number of key-value pairs in the dictionary: "))
for i in range(n):
    key=input("Key: ")
    value=input("Value: ")
    dict[key]=value
print("The elements dictionary elements are as follows: ")
print("Key : Value")
for key in dict:
    print(f" {key}  :  {dict[key]}")