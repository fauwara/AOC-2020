input_ = open('input.txt')

fuel = 0
for module_weight in input_:
    fuel = fuel + ( int(int(module_weight)/3) - 2 )

print(fuel)