import math
def num_of_digits(num):
	if num == 0:
		return 1
	return int(math.log10(abs(num))+1)