a = float(input("Enter 1st Side"))
b = float(input("Enter 2nd Side"))
c = float(input("Enter 3rd Side"))
s = (a + b + c) / 2
area = (s*(s-a)*(s-b)*(s-c)) /2
area = format(area, '.2f')
print("The Area of the Triangle is : ",area)