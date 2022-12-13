# counter = 0
# cycle_counter = 0
# signal_strength = 0

# sprite_position = 1

# with open('input.txt') as input_:
# 	for i in input_:
# 		if i[:4] == 'addx':
# 			command, size = i.split()

# 			for i in range(2):
# 				cycle_counter += 1
# 				if cycle_counter in [20, 60, 100, 140, 180, 220]:
# 					# print(f'{cycle_counter}: {x} * {cycle_counter} = {signal_strength}')
# 					signal_strength += x*cycle_counter

# 				# if x >= sprite_position-1 and x <= sprite_position+1: print('.')
# 				# else: print('#')

# 			x += int(size)

# 		else:
# 			cycle_counter += 1
# 			counter += 1

# 			if cycle_counter in [20, 60, 100, 140, 180, 220]:
# 				# print(f'{cycle_counter}: {x} * {cycle_counter} = {signal_strength}')
# 				signal_strength += x*cycle_counter

# 			# if x >= sprite_position-1 and x <= sprite_position+1: print('.')
# 			# else: print('#')

# print(signal_strength)


x = 2
row = 0
column = 0

cycle = 1

with open('input.txt') as input_:
	for i in input_:
		if i[:4] == 'addx':
			command, size = i.split()
			
			for i in range(2):
				
				# print pixel
				if cycle >= x-1 and cycle <= x+1:
					print('█', end='')
				else: 
					print(' ', end='')

				if cycle%40 == 0:
					cycle = 0
					print()

				cycle +=   1
				
			
			x += int(size)
		
		else:

			# print pixel
			if cycle >= x-1 and cycle <= x+1:
				print('█', end='')
			else: 
				print(' ', end='')
			
			if cycle%40 == 0:
				cycle = 0
				print()

			cycle += 1