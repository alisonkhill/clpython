# range(start, stop, step)
# for example:
    #range(7) = 1, 2, 3, 4, 5, 6, 7
    #range(1,7,1) = same as range(7)
    #range(2, 14, 2) = 2, 4, 6, 8, 10, 12, 14


total = 0
expenses = []
num_expenses = int(input("Enter # of Expenses "))

for i in range(num_expenses):
    expenses.append(float(input("Enter your expense: ")))

total = sum(expenses)
print("You spent $", total, sep = '')