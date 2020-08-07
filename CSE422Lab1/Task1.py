ParcentValue = input("Enter Parcentage")
value = int(ParcentValue[0:(len(ParcentValue)-1)]) # slicing upto %
print("Equivalent Decimal", value/100)
