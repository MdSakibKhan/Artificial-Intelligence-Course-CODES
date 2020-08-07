sum = 0
count = 0
for i in range(0, 100):
    if i % 3 == 0:
        count+=1
        sum+=i
print("Average :", (sum/count))