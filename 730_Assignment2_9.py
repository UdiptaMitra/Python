'''Write a Python program to reverse a list using iteration without using built-in functions'''
l1=[]
n_list=int(input("enter total number of elements in the list "))
for i in range(n_list):
    elem=int(input("enter element "+str(i+1)+" "))
    l1.append(elem)
for i in range(0,int(n_list/2)):
    temp=l1[i]
    l1[i]=l1[n_list-1-i]
    l1[n_list-1-i]=temp
print("The reversed list is: ",l1)