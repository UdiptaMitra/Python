'''Write a recursive function to find the maximum element in a list'''
list1=[]
n_list=int(input("Enter total number of elements in the list: "))
for i in range(n_list):
    elem=int(input("enter element "+str(i+1)+" "))
    list1.append(elem)
max=0
def find_max(list1,max):
    if len(list1)==0:
        return max
    else:
        elem=list1.pop()
        if max<elem:
            max=elem
        return find_max(list1,max)
print("The maximum of the elements in the list is: ",find_max(list1,max))