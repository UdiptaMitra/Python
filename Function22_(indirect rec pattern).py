# 12345 31 23456 42 34567 53
#player a increases value by 1 five times, player b decreses value by 2 two times
#total turns of both player combined guven by user

'''def func_increase(n):
    if n==0:
    for i in range(5):
        print(i)
    func_decrease(n-1)

def func_decrease(n):
    for i in range(n,n-4,-2):
        print(i)
    func_increase(n-1)

func_increase(1)'''


def playerA(n,i=1):
    if n==0:
        return
    for i in range(i,i+5,1):
        print(i,end=" ")
    print("Player A's turn")
    playerB(n-1,i)
def playerB(n,i=1):
    if n==0:
        return
    for i in range(i,i-4,-2):
        print(i,end=" ")
    print("Player B's turn")
    playerA(n-1,i-1)
playerA(6)

while(i<=5):
    print(i,end="")
    i+=1