'''Write a Python program to find the top K frequent elements in a list'''
list1=eval(input("Enter a list (elements enclosed in [] separated by ,): "))
list1.sort()
grouped=[]
freq_list=[]
i=0
while i<len(list1):
    val=list1[i]
    temp=[]
    while i<len(list1) and list1[i]==val:
        temp.append(list1[i])
        i+=1
    grouped.append(temp)
print(grouped)
for i in range(len(grouped)):
    freq_list.append((len(grouped[i]),grouped[i][0]))
print(freq_list)
k=int(input("Enter the value of k: "))
if k<=len(freq_list):
    freq_list.sort(reverse=True)
    print("Top",k,"frequent elements:")
    for i in range(k):
        print(freq_list[i][1])
else:
    print("k is larger than total unique elements")