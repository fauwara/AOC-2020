# formatting input
with open('input.txt') as input_:
    input_list = []
    for i in input_:
        input_values = ['','','','']
        input_splited = i.split(':')
        input_values[3] = input_splited[1] # Password to be validated
        input_splited = input_splited[0].split(' ')   
        input_values[2] = input_splited[1] # Letter to be checked
        input_splited = input_splited[0].split('-')  
        input_values[1] = int(input_splited[1]) # max letter count and string index for part 2
        input_values[0] = int(input_splited[0]) # min letter count and string index for part 2
        input_list.append(input_values)

# print(input_list)
# Part - 1
count = 0
for input_ in input_list:
    letter_count = 0
    for j in range(len(input_[3])):
        if input_[2] == input_[3][j]:
            letter_count += 1
    
    if letter_count >= input_[0] and letter_count <= input_[1]:
        count += 1

print(f'count:{count}')

# Part - 2
count = 0
for input_ in input_list:
    status_1 = False
    status_2 = False
    # print(input_)
    if input_[2] == input_[3][input_[0]]:
        status_1 = True
    if input_[2] == input_[3][input_[1]]:
        status_2 = True

    if status_1 != status_2:
        count += 1

print(f'count:{count}')