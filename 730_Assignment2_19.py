'''Write a Python program to create a custom iterator that generates numbers from 1 to N'''

class NaturalNumber:
    def __init__(self, n):
        self.n=1
    def __iter__(self):
        return self
    def __next__(self):
        x=self.n
        self.n+=1
        return x
n=int(input("Enteer the limiting value n: "))
num=NaturalNumber(n)
it=iter(num)
for i in range(n):
    print(next(it))
