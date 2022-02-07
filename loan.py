# Get the loan details from the user

money_owed = float(input("how much money do you owe in dollars?\n")) #50,000
apr = float(input("What is the annual percentage rate?\n")) #3
payment = float(input("What is your monthly payment?\n")) #1,000
months = int(input("how many months should we calculate for?\n")) #24

# Calculate montly interest rate: divide apr by 100, then divide that by 12

monthly_rate = apr/100/12

for i in range(months):

    # Add interest we need to pay - monthly_rate times money_owed, increment to money_owed total
    interest = monthly_rate * money_owed
    money_owed = money_owed + interest

    if (money_owed - payment < 0):
        print("The last payment is $", money_owed, sep = '')
        print("You paid off the loan in", i+1, "months.")
        break

    # Take monthly payments into account
    money_owed = money_owed - payment

    # Print the results
    print("You paid $", payment, ", of which $", interest, " was interest.", sep = '', end=' ')
    print("Now you owe $", money_owed)

