# Calculate tip

bill_amount = float(input("Total bill amount?  "))
service_level = input("Level of service?  ")

if service_level == "good":
    good_tip = bill_amount * .2
    print("Tip amount: $" + str("{:.2f}".format(good_tip)))
    total_amount = good_tip + bill_amount
    print("=====")
    print("Total amount: $" + str(total_amount))

elif service_level == "fair":
    fair_tip = bill_amount * .15
    print("Tip amount: $" + str("{:.2f}".format(fair_tip)))
    total_amount = fair_tip + bill_amount
    print("=====")
    print("Total amount: $" + str(total_amount))

elif service_level == "poor":
    poor_tip = bill_amount * .10
    print("Tip amount: $" + str("{:.2f}".format(poor_tip)))
    total_amount = poor_tip + bill_amount
    print("=====")
    print("Total amount: $" + str(total_amount))