map_ = []

#reading input and store in map_ as 2d array
with open('input.txt') as input_map:
	for row in input_map:
		row = list(map(int, list(row.replace('\n',''))))
		map_.append(row)

h = len(map_)
w = len(map_[0])

count = w*2 + h*2 -4

def res_1():
	for y in range(1,h-1):
		for x in range(1,w-1):
			temp_x = x-1
			temp_y = y-1

			visible_left = 1
			visible_right = 1
			visible_up = 1
			visible_down = 1
			
			# left
			while visible_left and (temp_x >= 0):
				if map_[y][x] <= map_[y][temp_x]:
					visible_left = 0
				else: temp_x -= 1
			temp_x = x+1

			# right
			while visible_right and (temp_x < w):
				if map_[y][x] <= map_[y][temp_x]:
					visible_right = 0
				else: temp_x += 1

			# up
			while visible_up and (temp_y >= 0):
				if map_[y][x] <= map_[temp_y][x]:
					visible_up = 0
				else: temp_y -= 1
			temp_y = y+1
			
			# down
			while visible_down and (temp_y < h):
				if map_[y][x] <= map_[temp_y][x]:
					visible_down = 0
				else: temp_y += 1
			
			if visible_left or visible_right or visible_up or visible_down:
				count +=1
	return count


# * PART 2
# The above code could be written like part 2 code but it works for now so imma leave it as it is

# left  (x_inc, y_inc) => (-1,  0)
# right (x_inc, y_inc) => ( 1,  0)
# up    (x_inc, y_inc) => ( 0, -1)
# down  (x_inc, y_inc) => ( 0,  1)

def count_tree_score( x, y, x_inc, y_inc ):

	directional_tree_score = 0
	temp_x = x
	temp_y = y

	temp_x += x_inc
	temp_y += y_inc

	while (temp_x >= 0 and temp_x < w) and (temp_y >= 0 and temp_y < h):

		if map_[y][x] <= map_[temp_y][temp_x]:
			directional_tree_score += 1
			break
		else: directional_tree_score += 1
	
		temp_x += x_inc
		temp_y += y_inc
	
	return directional_tree_score


# print(count_tree_score( 2, 3, 0, -1))

def res_2():
	
	max_tree_score = 0
	for y in range(0,h-1):
		for x in range(0,w-1):
			
			tree_score = 1

			tree_score *= count_tree_score(x, y, -1,  0) # left
			tree_score *= count_tree_score(x, y,  1,  0) # right
			tree_score *= count_tree_score(x, y,  0, -1) # up
			tree_score *= count_tree_score(x, y,  0,  1) # down
		
			max_tree_score = max(max_tree_score, tree_score)
	
	return max_tree_score

# print(res_1())
print(res_2())