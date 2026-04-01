'''Write a Python program to count the occurrence of each word in a given sentence using a dictionary'''
string1=input("Enter a string: ")
list1=string1.split()
count_words={}
for i in range(len(list1)):
    count=0
    if list1[i] not in list1[:i]:
        for j in range(i,len(list1)):
            if list1[i]==list1[j]:
                count+=1
    if count>0:
        count_words[list1[i]]=count
print(count_words)