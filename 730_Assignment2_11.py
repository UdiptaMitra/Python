'''Write a Python program to create a set and iterate through it to print all unique elements'''
n=int(input("Enter total number of elements: "))
set1=set()
for i in range(n):
    elem = input("Enter element: ")
    set1.add(elem)
print("The elements of the set are as follows: ")
for item in set1:
    print(item)