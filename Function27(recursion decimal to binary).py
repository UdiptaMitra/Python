#recursive function to convert decimal number to binary number
import math
decimal=int(input("Enter a decimal number: "))
rem=''
def toBinary(decimal,rem):
    rem=rem+str(decimal%2)
    if decimal==1:
        print(rem[::-1])
        return
    else:
        toBinary((math.floor(decimal/2)),rem)
        return
toBinary(decimal,rem)