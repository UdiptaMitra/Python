'''Write a Python program to find the maximum and minimum elements in a list.'''
list1=[]
n_list=int(input("enter total number of elements in the list "))
for i in range(n_list):
    elem=int(input("enter element "+str(i+1)+" "))
    list1.append(elem)
print("The maximum of all the elements is: ",max(list1))
print("The minimum of all the elements is: ",min(list1))

    
    
