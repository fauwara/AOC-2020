list_ = [0,0,0]

with open("input.txt") as input_:
	count = 0
	for i in input_:
		if i == "\n":
			list_ = sorted(list_, reverse=True)
			if count > list_[-1]:
				list_[-1] = count
			count = 0
		else: count += int(i)

	# max_ = max(count, max_)
	list_ = sorted(list_, reverse=True)
	if count > list_[-1]:
		list_[-1] = count

print(sum(list_))