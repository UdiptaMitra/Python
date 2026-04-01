'''Write a Python program to print numbers from 1 to 20 along with their squares using the range() function'''
list1=list(map(lambda x:(x,x*x),range (1,21)))
print("The required output in list of tuples form is: ",list1)
