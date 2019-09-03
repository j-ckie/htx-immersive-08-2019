# Do you want more coins?
coin_num = 0
print("You have " + str(coin_num) + " coins.")
coins = input("Do you want another?  ")

while coins == "yes":
    coin_num += 1
    print("You have " + str(coin_num) + " coins.")
    coins = input("Do you want another?  ")

print("Bye")