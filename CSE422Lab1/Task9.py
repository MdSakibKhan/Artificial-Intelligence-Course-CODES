import numpy as np
list= [2,4,1,5,6,8,10,40,9,11]
list = np.array(list)
avg = list.sum()/list.size
small = list.min()
large = list.max()
print("The Difference between Average Number and Smallest number is : ", np.abs(avg-small))
print("The Difference between Average Number and Largest number is : ", np.abs(avg-large))

