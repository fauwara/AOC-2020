# .234.....  2-4
# .....678.  6-8

# .23......  2-3
# ...45....  4-5

# ....567..  5-7
# ......789  7-9

# .2345678.  2-8
# ..34567..  3-7

# .....6...  6-6
# ...456...  4-6

# .23456...  2-6
# ...45678.  4-8

# ..34567..  3-7
# .2345678.  2-8

def filter_input(input):
	
	elf1, elf2 = input.split(',')
	elf2 = elf2.replace('\n','')
	
	elf1 = elf1.split('-')
	elf2 = elf2.split('-')

	elf1 = [int(elf1[0]), int(elf1[1])]
	elf2 = [int(elf2[0]), int(elf2[1])]

	min_elf, max_elf = (elf1, elf2) if elf1[0]<elf2[0] else (elf2, elf1)

	return min_elf, max_elf


with open('input.txt') as input_:
	count = 0
	for line in input_:
		min_elf, max_elf = filter_input(line)

		if min_elf[1] >= max_elf[0]:
			print(min_elf, max_elf)
			count += 1
		# if ( elf1[0] <= elf2[0] and elf1[1] >= elf2[1] ) or ( elf1[0] >= elf2[0] and elf1[1] <= elf2[1] ):
			# print(min_elf, max_elf)
			# count += 1

print(count)