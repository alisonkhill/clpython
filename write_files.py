
# assign a variable to open the file and indicate a mode (w, r, a)
# if the file doesn't exist, python will create it
sales_log = open('spam_orders.txt', 'w') # w is for write, r is read, a for append

# write to the file
sales_log.write('The Spam Van\n')
sales_log.write('Sales Log')

# close the file
sales_log.close()


# EXAMPLE
def write_sales_log(order):
    # open/create file
    file = open('sales.txt', 'a')

    total = 0

    for item, price in order.items():
        file.write(item + ' ' + format(price, '.2f') + '\n')
        total += price

    file.write('total = ' + format(total, '.2f') + '\n\n')

    file.close()

def main():
    order = {'Cheeky Spam': 1.0,'Yonks Spam': 4.0}
    write_sales_log(order)
    order = {'Cheerio Spam': 1.0, 'Smashing Spam': 3.0}
    write_sales_log(order)

main()