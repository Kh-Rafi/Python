# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

def find_angle(ab,bc):
    angle_radians = math.atan2(ab, bc)
    angle_degrees = math.degrees(angle_radians)

    return int(angle_degrees + 0.5)



if __name__ == '__main__':

    ab = int(input().strip())
    bc = int(input().strip())

    print(f"{find_angle(ab, bc)}\u00b0")
