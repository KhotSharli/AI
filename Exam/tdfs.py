def tower_of_hanoi(n,source,destination,aux):
    if n==1:
        print(f"Move 1 from {source} to {destination}")
        return
        
    tower_of_hanoi(n-1,source,aux,destination)
    
    print(f"Move {n} from {source} to {destination}")
    
    tower_of_hanoi(n-1,aux,destination,source)
    
def solve(n):
    print(f"This has {n} pegs")
    tower_of_hanoi(n,"A","C","B")
    
n=3
solve(n)