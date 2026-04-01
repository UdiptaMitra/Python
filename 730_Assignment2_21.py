'''Write a Python program to find two numbers in a list that add up to a given target value (Two Sum problem)'''
list1=[]
two_sum=[]
flag=0

#approach 1 
n_list=int(input("Enter total number of elements in the list: "))
for i in range(n_list):
    elem=int(input("enter element "+str(i+1)+" "))
    list1.append(elem)
target=int(input("enter the value of target sum: "))
for i in range(n_list):
    for j in range(n_list):
        if i!=j:
            two_sum.append((list1[i],list1[j]))

for item in two_sum:
    if sum(item)==target:
        flag=1
        target_tuple=item
        break
if flag==1:
    print("Target sum present (approach 1) : ",target_tuple)
else:
    print("Target sum not present (approach 1)")

#approach 2 (better)
for num1 in list1:
    num2=target-num1
    if num2 in list1:
        flag=1
        break
if flag==1:
    print("Target sum present (approach 2): ",(num1,num2))
else:
    print("Target sum not present (approach 2)")