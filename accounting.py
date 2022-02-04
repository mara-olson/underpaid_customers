melon_cost = 1.00
#sets the price of a melon

def paid_melons(payment_file):
    file = open(payment_file)
#select the file of orders to sue
    for line in file:
    #for each line item
        line = line.rstrip()
        #strip any padding off the end of each line
        row = line.split("\n")
        #define a different entry on a different lines as its own row
        words = line.split("|")
        #define words as the items separated by the symbol "|"
        cust_no, customer, melons, payment = words
        #each line item is composed of a customer number, customer name, melon, and payment
        melons = float(melons)
        #make sure we have decimals persist to price
        payment = float(payment)
        #make sure we have decimals persist to price
        expected_payment = melons * melon_cost
        #calculating multiple here to avoid later redundancy
        for customer in row:
        #for each customer
            if expected_payment == payment:
                payment_status = "paid correctly"
            elif expected_payment > payment:
                payment_status = "overpaid"
            elif expected_payment < payment:
                payment_status = "underpaid"
            #setting payment statuses based on <=> of what a certain number of melons costs
            print(f"{words[1]} {payment_status}. Expected payment was ${melon_cost * melons}, payment was ${payment}.")      
            #print a message so we know which customers paid what
    file.close()

paid_melons("customer-orders.txt")
# customer1_name = "Joe"
# customer1_melons = 5
# customer1_paid = 5.00

# customer2_name = "Frank"
# customer2_melons = 6
# customer2_paid = 6.00

# customer3_name = "Sally"
# customer3_melons = 3
# customer3_paid = 3.00

# customer4_name = "Sean"
# customer4_melons = 9
# customer4_paid = 9.50

# customer5_name = "David"
# customer5_melons = 4
# customer5_paid = 4.00

# customer6_name = "Ashley"
# customer6_melons = 3
# customer6_paid = 2.00

# customer1_expected = customer1_melons * melon_cost
# if customer1_expected != customer1_paid:
#     print(f"{customer1_name} paid ${customer1_paid:.2f},",
#           f"expected ${customer1_expected:.2f}"
#           )

# customer2_expected = customer2_melons * melon_cost
# if customer2_expected != customer2_paid:
#     print(f"{customer2_name} paid ${customer2_paid:.2f},",
#           f"expected ${customer2_expected:.2f}"
#           )

# customer3_expected = customer3_melons * melon_cost
# if customer3_expected != customer3_paid:
#     print(f"{customer3_name} paid ${customer3_paid:.2f},",
#           f"expected ${customer3_expected:.2f}"
#           )

# customer4_expected = customer4_melons * melon_cost
# if customer4_expected != customer4_paid:
#     print(f"{customer4_name} paid ${customer4_paid:.2f},",
#           f"expected ${customer4_expected:.2f}"
#           )

# customer5_expected = customer5_melons * melon_cost
# if customer5_expected != customer5_paid:
#     print(f"{customer5_name} paid ${customer5_paid:.2f},",
#           f"expected ${customer5_expected:.2f}"
#           )

# customer6_expected = customer6_melons * melon_cost
# if customer6_expected != customer6_paid:
#     print(f"{customer6_name} paid ${customer6_paid:.2f},",
#           f"expected ${customer6_expected:.2f}"
#           )
