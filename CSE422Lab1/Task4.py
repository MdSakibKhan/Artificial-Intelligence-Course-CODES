copies = int(input("Enter Number of copies"))
Cost = 0
if copies<100:
    Cost = 100*50
else:
    Cost = 100*50
    remaining = copies-100
    Cost = Cost+(remaining*30)
print("Total Cost :",Cost)