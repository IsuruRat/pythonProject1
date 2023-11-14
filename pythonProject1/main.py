h = int(input("enter your height"))

if h > 120:
    print("you can ride")
    age = int(input("what is your age?"))
    p = int(input("want a photo?"))
    if age <= 12:
        if p == 1:
            print("pay 8")
        else:
            print("pay 5")

    elif age > 1:
        if p == 10:
            print("pay 15")
        else:
            print("pay 12")

    else:
        if p == 1:
            print("pay 10")
        else:
            print("pay 7")

else:
    print("you cant ride")

