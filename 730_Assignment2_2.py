'''Write a Python program to find the sum of all elements in a given list.'''
list1=[]
n_list=int(input("enter total number of elements in the list "))
for i in range(n_list):
    elem=int(input("enter element "+str(i+1)+" "))
    list1.append(elem)
print("The sum of all the elements is: ",sum(list1))

    
    
