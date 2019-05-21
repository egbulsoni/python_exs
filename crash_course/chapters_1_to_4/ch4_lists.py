nums_til_twenty = list(range(1,21))
for n in nums_til_twenty:
    print(n)

one_million_nums = list(range(1,1000001))
for n in one_million_nums:
    print(n)

print(min(one_million_nums))
print(max(one_million_nums))
print(sum(one_million_nums))

odd_til_twenty = range(1,20,2)
for n in odd_til_twenty:
    print(n)

mult_3 = range(3,31,3)
for n in mult_3:
    print(n)

cubes = range(1,11)
for cube in cubes:
    print(cube**3)

cubes_comprehension = [n ** 3 for n in range(1,11)]
print(cubes_comprehension)



