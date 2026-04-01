'''Write a recursive function to solve the Tower of Hanoi problem and print the moves'''

'''The Tower of Hanoi is a classic mathematical puzzle involving three rods (A, B, and C) and n disks of different sizes.
 Initially, all disks are stacked on rod A in decreasing order of diameter - the largest disk at the bottom and the smallest at the top.
Goal is to move the entire stack to another rod (rod C) while following these rules:
Move only one disk at a time.
At each step, you can take the top disk from any rod and place it on another rod.
A disk can only be moved if it is the topmost disk of a rod.
No larger disk may be placed on top of a smaller disk.'''

ring=int(input("Enter the total number of rings: "))
moves=0
def min_moves(ring,moves):
    if ring==1:
        return 1
    moves=1+2*min_moves(ring-1,moves) #n-1 from source to helper, last 1 disc to destination, n-1 from helper to destination
    return moves
print(f"The total number of minimum moves for {ring} rings is {min_moves(ring,moves)} ")

def tower_hanoi(ring,init_rod,help_rod,fin_rod):
    if ring==1:
        print(f" Ring {ring} moves from {init_rod} to {fin_rod} ")
        return 
    tower_hanoi(ring-1, init_rod, fin_rod, help_rod)
    print(f" Ring {ring} moves from {init_rod} to {fin_rod} ")
    tower_hanoi(ring-1, help_rod, init_rod, fin_rod)
tower_hanoi(ring,'Rod_start','Rod_help','Rod_end')
