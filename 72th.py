from collections import deque

def can_stack_cubes():
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        cubes = deque(map(int, input().split()))
        
        current_top = float('inf')
        possible = True
        
        while cubes:
            if cubes[0] >= cubes[-1]:
                picked = cubes.popleft()
            else:
                picked = cubes.pop()
                
            if picked > current_top:
                possible = False
                break
            
            current_top = picked
    
        if possible:
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    can_stack_cubes()
