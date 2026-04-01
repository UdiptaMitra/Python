'''Write a Python program to count the frequency of each element in a list'''
l1=[]
freq_dist=[]
n_list=int(input("enter total number of elements in the list "))
for i in range(n_list):
    elem=int(input("enter element "+str(i+1)+" "))
    l1.append(elem)
for i in range(n_list):
    count=0
    if l1[i] not in l1[:i]:
        for j in range(i,n_list):
            if l1[i]==l1[j]:
                count+=1
    if count>0:
        freq_dist.append((l1[i],count))
print(freq_dist)
            
