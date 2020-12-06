from os import path, mkdir


status = True
while status:
    day = input('day > ')

    try:
        mkdir(f'2020/day-{day}',0o777)
        py_file = open(f'2020/day-{day}/index.py','w')
        input_file = open(f'2020/day-{day}/input.txt','w')
        md_file = open(f'2020/day-{day}/README.md','w')
        status = False
    except FileExistsError:
        print('The directory already exists.\n Try again.')