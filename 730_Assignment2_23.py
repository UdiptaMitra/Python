'''Write a Python program to group a list of strings into anagrams (e.g., ["eat", "tea", "tan"])'''
'''sample input - 6 elements
ate
listen
eat
tea
silent
imagine'''

list1=[]
anagram=[]
anagram_grouped=[]
n_list=int(input("enter total number of elements in the list "))
for i in range(n_list):
    elem=input("enter element "+str(i+1)+" ")
    list1.append(elem)
for i in range(n_list):
    for j in range(i+1,n_list):
        if sorted(list1[i])==sorted(list1[j]):
            if list1[i] not in anagram:
                anagram.append(list1[i])
            if list1[j] not in anagram:
                anagram.append(list1[j])
for i in range(len(anagram)):
    current=[anagram[i]]
    for j in range(i+1,len(anagram)):
        if sorted(anagram[i])==sorted(anagram[j]):
            if anagram[j] not in current:
                current.append(anagram[j])
    if len(current)>1:
        if current not in anagram_grouped:
            anagram_grouped.append(current)
print(anagram_grouped)

