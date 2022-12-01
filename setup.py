from os import path, getcwd, mkdir


status = True
while status:
    day = input('day > ')
    year = 2022
    # year = input('year > ')

    aoc_path = path.join(getcwd(), f"{year}/day-{day}")

    try:
        mkdir(aoc_path)
        py_file = open(f'{year}/day-{day}/index.py','w')
        input_file = open(f'{year}/day-{day}/input.txt','w')
        md_file = open(f'{year}/day-{day}/README.md','w')
        status = False
    except FileExistsError:
        print('The directory already exists.\n Try again.')