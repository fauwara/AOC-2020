
# Part - 2

slopes_part_1 = [[3,1]]  
slopes_part_2 = [[1,1],[3,1],[5,1],[7,1],[1,2]]  

with open('input.txt') as grid:
    grid = grid.readlines()

def crash_count(slopes):
    res = 1
    for slope in slopes:
        current_position_x = 0
        count = 0
        for row in grid[::slope[1]]:
            if row[current_position_x] == '#':
                count += 1
            current_position_x += slope[0]
            # -1 cuz the input contains a \n at the end 
            if current_position_x >= (len(row)-1):
                current_position_x = current_position_x - (len(row)-1)
        res *= count

print(f'Part - 1: {crash_count(slopes_part_1)}')
print(f'Part - 1: {crash_count(slopes_part_2)}')