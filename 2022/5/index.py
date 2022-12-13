num_crates = 3
crates = [ [] for i in range(num_crates)]

def reverse(lst):
    return lst[::-1]

with open('input.txt') as input_:
	# store crates in stack
	for i in input_:
		
		if i[1] == '1':
			break
		
		for j in range(num_crates):
			if not i[ 1+(j*4) ] == ' ':
				crates[j].append(i[ 1+(j*4) ])

	crates = list(map( lambda lst: lst[::-1], crates))

	# directions
	for i in input_:
		if i != "\n":
			dir_ = i.split()
			dir_.pop(0)
			dir_.pop(1)
			dir_.pop(2)
			dir_ = list(map(int, dir_))
			# print(dir_)

			# for i in crates:
			# 	print(i)
			# print()

			for i in range(dir_[0]):
				temp = crates[dir_[1]-1].pop()
				crates[dir_[2]-1].append(temp)

# for i in crates:
# 	print(i)
# print()

for i in crates:
	print(i[-1], end='')
print()