'''Write a Python program to perform union, intersection, and difference operations on two sets'''

n1=int(input("Enter total number of elements for set 1: "))
set1=set()
for i in range(n1):
    elem = input("Enter element: ")
    set1.add(elem)

n2=int(input("Enter total number of elements for set 2: "))
set2=set()
for i in range(n2):
    elem = input("Enter element: ")
    set2.add(elem)

print("The union of the two sets is: ",set1|set2)
print("The intersection of the two sets is: ",set1&set2)
print("The set difference set1 - set2 is : ",set1-set2)
print("The set difference set2 - set1 is : ",set2-set1)
print("The symmetric difference of the two sets is : ",set2^set1)