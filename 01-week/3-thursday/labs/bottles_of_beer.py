import time

def main():

    bottles_of_beer = 99
    first = "bottles of beer"
    second = "on the wall"
    third = "take one down"
    fourth = "pass it around"


    while bottles_of_beer > 1:
        if bottles_of_beer > 1:
            print(str(bottles_of_beer) + " " + first + " " + second)
            time.sleep(1)
            print(str(bottles_of_beer) + " " + first)
            time.sleep(2)
            print(third)
            time.sleep(1)
            print(fourth)
            time.sleep(1)
            bottles_of_beer -= 1
            print(str(bottles_of_beer) + " " + first + " " + second)
            time.sleep(2)

    print("No more bottles of beer")
    time.sleep(1)
    print("on the wall")
    time.sleep(1)
    print("no more bottles of beer")
    time.sleep(2)
    print("Go to the store")
    time.sleep(1)
    print("buy some more")

    restart = input("How many bottles of beer on the wall?   ")
    if restart == "99":
        main()
    
    else:
        print("Go home, you're drunk")

main()