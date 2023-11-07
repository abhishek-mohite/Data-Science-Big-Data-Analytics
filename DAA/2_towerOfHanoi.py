# Recursive Python function to solve tower of hanoi 
#he Tower of Hanoi is a classic problem in computer science and mathematics that involves moving a set of disks from one rod to another while following certain rules.
#The problem consists of three rods (A, B, and C) and a number of disks of different sizes, initially stacked in decreasing order of size on one rod.
#objective , rules
def TowerOfHanoi(n, from_rod, to_rod, aux_rod): 
	if n == 0: 
		return
	TowerOfHanoi(n-1, from_rod, aux_rod, to_rod) 
	print("Move disk", n, "from rod", from_rod, "to rod", to_rod) 
	TowerOfHanoi(n-1, aux_rod, to_rod, from_rod) 


# driver code
N = 3

# A, C, B are the name of rods 
TowerOfHanoi(N, 'A', 'C', 'B') 

