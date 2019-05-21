for i in range(1,21):
    print(i)

nums = list(range(1,1000001))
print(min(nums))
print(max(nums))
print(sum(nums))
#for n in nums:
#    print(n)
odd_nums = list(range(1, 21, 2))
print(odd_nums)

threes = list(range(3, 31, 3))
for three in threes:
    print(three)

cubes = [value**3 for value in range(1,11)]
for cube in cubes:
    print(cube)
