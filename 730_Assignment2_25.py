'''Write a Python program to merge two sorted lists into a single sorted list without using built-in sorting functions'''

#run without debug because start debugging is causing some error

list1=eval(input("Enter a sorted list 1 (elements enclosed in [] separated by ,): "))
list2=eval(input("Enter a sorted list 2 (elements enclosed in [] separated by ,): "))

i=j=0
merged=[]

while(i<len(list1) and j<len(list2)):
    if(list1[i]<list2[j]):
        merged.append(list1[i])
        i+=1
    elif(list2[j]<list1[i]):
        merged.append(list2[j])
        j+=1
    else:
        merged.append(list1[i])
        i+=1
        merged.append(list2[j])
        j+=1

if(i==len(list1)):
    for p in range(j,len(list2)):
        merged.append(list2[p])
elif(j==len(list2)):
    for p in range(i,len(list1)):
        merged.append(list1[p])

print(merged)