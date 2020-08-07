year = int(input("Enter Year:"))
if year % 100 == 0:
    if year % 400 == 0:
        print("This is Leap Year")
    else:
        print("This is not Leap Year")
elif year % 4 == 0:
    print("This is Leap year")
else:
    print("This is not Leap Year")
