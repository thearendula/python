def toh(n, fromRod, toRod, auxRod):
    if n == 1:
        print("Move disk 1 from_Rod ", fromRod, " to_Rod ",toRod)
        return
    toh(n-1, fromRod, auxRod, toRod)
    print("Move disk ",n," from_Rod ", fromRod," to_Rod ", toRod)
    toh(n-1, auxRod, toRod, fromRod)
    

n = 3
toh(n,'A', 'C', 'B')