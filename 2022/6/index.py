input_ = open('input.txt', 'r').read()

marker_length = 14

for i in range(len(input_)): # start letter
	flag = 0
	for j in range(0,marker_length-1): # check letter in group 4
		for k in range(j+1,marker_length): # compare to letter above
			# print(i+j, i+j+k)
			if input_[i+j] == input_[i+k]:
				flag = 1
				break
	if not flag:
		print(i+marker_length)
		break