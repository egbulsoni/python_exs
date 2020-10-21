stair = int(input("Enter the number of the staircase's height: "))
while stair > 0:
    for i in range(1, stair+1):
        print(" " * int(stair-1), end='')
        print("#" * i)
        stair = stair - 1
    stair = stair - 1
