list_ = [0,0,0]

with open("input.txt") as input_:
	count = 0
	for i in input_:
		if i == "\n":
			list_ = sorted(list_)
			if count > list_[0]:
				list_[0] = count
			count = 0
		else: count += int(i)

	list_ = sorted(list_)
	if count > list_[0]:
		list_[0] = count

print(sum(list_))