# A, X - ROCK, LOSE
# B, Y - PAPER, DRAW
# C, Z - SCISSOR, WIN

# 0 - LOSS
# 3 - DRAW
# 6 - WIN

scores = {
	'loss' : 0,
	'draw' : 3,
	'winn' : 6,
}

rps_score = {
	'X': 1, 
	'Y': 2,
	'Z': 3,
}

rps_map_2 = {
	'A' : {
		'loss': rps_score['Z'],
		'draw': rps_score['X'],
		'winn': rps_score['Y'],
	},
	'B' : {
		'loss': rps_score['X'],
		'draw': rps_score['Y'],
		'winn': rps_score['Z'],
	},
	'C' : {
		'loss': rps_score['Y'],
		'draw': rps_score['Z'],
		'winn': rps_score['X'],
	},
}

with open("input.txt") as input_:
	res = 0
	for i in input_:
		inp = i.split()
		if inp[1] == 'X': # LOSE
			res += scores['loss']
			res += rps_map_2[inp[0]]['loss']
		elif inp[1] == 'Y': # DRAW
			res += scores['draw']
			res += rps_map_2[inp[0]]['draw']
		else: # WIN
			res += scores['winn']
			res += rps_map_2[inp[0]]['winn']

print(res)
		