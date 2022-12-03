with open('input.txt') as input_:
	sum = 0
	count = 0
	rucksacks = []
	badge = set('')
	
	for i in input_:
		rucksacks.append(set(i) - set('\n'))
		
		count += 1
		if count >= 3:
			badge = rucksacks[0]
			for j in range(1, len(rucksacks)):
				badge = badge & rucksacks[j]
			count = 0
			rucksacks = []
			badge = list(badge)[0]
			# inter = list(set(i[ : int(len(i)/2) ]) & set(i[ int(len(i)/2) : -1]))[0]
		
			if ord(badge) > 96:
				sum += ord(badge) - 96
			else: 
				sum += ord(badge) - 64 + 26

			# ni = ''
		
print(sum)