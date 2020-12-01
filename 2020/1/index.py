input_ = open('input.txt','r')

expense_list = []
for expense in input_:
    expense_list.append(int(expense))

input_.close()

for i in range(len(expense_list)):
    for j in range(len(expense_list)-i):
        if expense_list[i] + expense_list[i+j] == 2020:
            print(expense_list[i]*expense_list[i+j])
            break

