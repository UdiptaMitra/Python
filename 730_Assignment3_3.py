'''Write a recursive function to count the number of digits in a number'''
num=int(input("Enter a number: "))
count=0
def count_dig(num,count):
    if num==0:
        return count
    else:
        count+=1
        return count_dig(num//10,count)
print("The number of digits in a number is: ",count_dig(num,count))