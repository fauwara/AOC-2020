# # import sys
# # sys.setrecursionlimit(1500)

# class node():
# 	def __init__( self, name, parent):
# 		self.name = name
# 		self.parent = parent
# 		self.dirs  = []
# 		self.files = []

# class directory():
# 	def __init__(self):
# 		self.nodes = [node('/', 0)]
# 		self.index = 0

# ls_flag = 0
# dir_ = directory()

# with open('input.txt') as input_: # read input line by line
# 	for i in input_:

# 		if i[0] == '$':
# 			ls_flag = 0
		
# 		if ls_flag:
# 			i = i.split(' ')
# 			i[1] = i[1].replace('\n','') # remove \n at the end
# 			if i[0] == 'dir':
# 				dir_.nodes[dir_.index].dirs.append(node(i[1], dir_.index))
# 			else:
# 				dir_.nodes[dir_.index].files.append(int(i[0]))

# 		else:
# 			if i == '$ cd ..\n':
# 				dir_.index = dir_.nodes[dir_.index].parent
# 			elif i[:4] == '$ cd': # create directories
# 				dir_name = i[5:-1]
# 				if dir_name != '/':
# 					dir_.nodes.append(node(dir_name, dir_.index))
# 					dir_.index = len(dir_.nodes)-1

# 			elif i == '$ ls\n': # list directories
# 				ls_flag = 1

# 		# for j in dir_.nodes:
# 		# 	print('dir name:', j.name)
# 		# 	print('dir parent:', dir_.nodes[j.parent].name)
# 		# 	print('dirs: ', end ='')
# 		# 	for k in j.dirs:
# 		# 		print(k.name, end='')
# 		# 	print()
# 		# 	print('files:', j.files)
# 		# 	print('-')
# 		# print()

# size = []

# def calc_sum(node):
# 	sum_ = sum(node.files)
# 	# print(f'{node.name} {sum_} {node.dirs}')

# 	if node.dirs == []:
# 		# print(f'{node.name} is empty')
# 		return sum_
	
# 	for i in node.dirs:
# 		for j in dir_.nodes:
# 			if i.name == j.name:
# 				sum_ += calc_sum(j)

# 	return sum_
# 	# return sum_ + sum(map(calc_sum, node.dirs))

# print(calc_sum(dir_.nodes[0]))


import sys
from collections import defaultdict
infile = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(infile).read().strip()
lines = [x for x in data.split('\n')]

# directory path -> total size of that directory (including subdirectories)
SZ = defaultdict(int)
path = []
for line in lines:
    words = line.strip().split()
    if words[1] == 'cd':
        if words[2] == '..':
            path.pop()
        else:
            path.append(words[2])
    elif words[1] == 'ls':
        continue
    elif words[0] == 'dir':
        continue
    else:
        sz = int(words[0])
        # Add this file's size to the current directory size *and* the size of all parents
        for i in range(1, len(path)+1):
            SZ['/'.join(path[:i])] += sz

max_used = 70000000 - 30000000
total_used = SZ['/']
need_to_free = total_used - max_used

p1 = 0
p2 = 1e9
for k,v in SZ.items():
    #print(k,v)
    if v <= 100000:
        p1 += v
    if v>=need_to_free:
        p2 = min(p2, v)
print(p1)
print(p2)