# import timeit
# print(timeit.timeit( stmt = code2, number = 1))

class board():
	def __init__(self, n):
		self.size = n-1
		self.grid = [[0 for i in range(n)] for i in range(n)]
		self.count = 0

	def display_board(self):
		for row in self.grid:
			for cell in row:
				if cell: print('#', end='')
				else: 	print('-', end='')
			print('')


class node():
	def __init__( self, x, y ):
		self.x = x
		self.y = y


b = board(500)

rope = []
rl = 10
for i in range(rl):
	rope.append(node(int(b.size/2), int(b.size/2)))

# head = node(int(b.size/2), int(b.size/2))
# tail = node(int(b.size/2), int(b.size/2))

direction_map = {
	'L': (-1,  0),
	'R': ( 1,  0),
	'U': ( 0, -1),
	'D': ( 0,  1),
}


def mark_map(dir, steps):
	for _ in range(steps):
		# debug
		# print(f"head: {(head.x, head.y)}")
		# print(f"tail: {(tail.x, tail.y)}")
		
		rope[0].x += direction_map[dir][0]
		rope[0].y += direction_map[dir][1]
		# print('0:' ,rope[0].x, rope[0].y)

		# debug
		# print(f"new head: {(head.x, head.y)}")

		dist_x = rope[0].x-rope[1].x
		dist_y = rope[0].y-rope[1].y
		# print(f'dist x: {dist_x}')
		# print(f'dist y: {dist_y}')

		for i in range(1,rl):
			# print('rl' ,rl)
			if not((abs(dist_x) in [0,1]) and (abs(dist_y) in [0,1])):
				# print("not connected")

				if dist_x < 0: 	rope[i].x += -1
				elif dist_x > 0: rope[i].x += 1
				
				if dist_y < 0: rope[i].y += -1
				elif dist_y > 0: rope[i].y += 1

			# print(i)
			# print(f"{i}:",rope[i].x, rope[i].y)
			# exit()
			if i != rl-1:
				# print(i)
				dist_x = rope[i].x-rope[i+1].x
				dist_y = rope[i].y-rope[i+1].y

		
		if not b.grid[rope[rl-1].y][rope[rl-1].x]:
			b.grid[rope[rl-1].y][rope[rl-1].x] = 1
			b.count += 1
		
		# print("3:",rope[rl-1].x, rope[rl-1].y, '\n')
		
		# debug
		# print(f"new tail: {(tail.x, tail.y)}")
		# print()


with open('input.txt') as input_:
	for i in input_:
		dir, steps = i.split()
		
		mark_map(dir, int(steps))
		# print(dir, steps)
		
		# debug
		# print(dir, steps)
		# print('head')
		# h.display_board()
		# print('tail')
		# b.display_board()


b.display_board()
print(b.count)

