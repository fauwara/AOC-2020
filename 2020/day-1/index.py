# First Part

expense_list = []

with open('input.txt') as input_:
    for i in input_:
        expense_list.append(int(i))

for i in range(len(expense_list)):
    for j in range(len(expense_list)-i):
        if expense_list[i] + expense_list[i+j] == 2020:
            print(expense_list[i]*expense_list[i+j])
            break

# Second Part

for i in range(len(expense_list)):
    for j in range(len(expense_list)-i):
        for k in range(len(expense_list)-(i+j)):
            if expense_list[i] + expense_list[i+j] + expense_list[i+j+k] == 2020:
                print(expense_list[i]*expense_list[i+j]*expense_list[i+j+k])
                break