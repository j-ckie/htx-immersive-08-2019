# Calculate tip and split amounts

bill_amount = float(input("Total bill amount?  "))
service_level = input("Level of service?  ")
num_split = float(input("Split how many ways?  "))

if service_level == "good":
    good_tip = bill_amount * .2
    print("Tip amount: $" + str("{:.2f}".format(good_tip)))
    total_amount = good_tip + bill_amount
    print("=====")
    print("Total amount: $" + str("{:.2f}".format(total_amount)))
    split_amount = total_amount / num_split
    print("Price per person:  $" + str("{:.2f}".format(split_amount)))

elif service_level == "fair":
    fair_tip = bill_amount * .15
    print("Tip amount: $" + str("{:.2f}".format(fair_tip)))
    total_amount = fair_tip + bill_amount
    print("=====")
    print("Total amount: $" + str("{:.2f}".format(total_amount)))
    split_amount = total_amount / num_split
    print("Price per person:  $" + str("{:.2f}".format(split_amount)))

elif service_level == "poor":
    poor_tip = bill_amount * .10
    print("Tip amount: $" + str("{:.2f}".format(poor_tip)))
    total_amount = poor_tip + bill_amount
    print("=====")
    print("Total amount: $" + str("{:.2f}".format(total_amount)))
    split_amount = total_amount / num_split
    print("Price per person:  $" + str("{:.2f}".format(split_amount)))