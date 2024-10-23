import numpy as np
import random as rd
import pandas as pd




# arr1 = np.random.randint(0, 10, 8)
# arr1 = arr1 **2
# print(arr1)
# # arr1 = np.sqrt(arr1)



# print(arr1.max(), arr1.argmax(), arr1.min(), arr1.argmin(), arr1.sum())


# arr2 = np.arange(1, 11)
# series = pd.Series(arr2)
# print(arr2)
#
# lst2 =  [i for i in range(1, 11)]
# index  = [f'No {i}' for i in range(1, 11)]
# lst2 = pd.Series(lst2)
#
# lst = pd.Series([rd.randrange(1, 20) for i in range(1, 11)])
#
# dict1 = {
#     'Name' : 'Sathesh',
#     'Age' : '25',
#     'Status' : 'Single',
#     'Girlfriend' : 'Faustina'
# }
#
# ser3 = np.ones((4, 4))
# ser3_index = ['One', 'Two', 'Three', 'Four']
# ser3_column = ['One', 'Two', 'Three', 'Four']
# ser3_column.reverse()
# ser3 = pd.DataFrame(ser3, ser3_index, ser3_column)
# print(ser3.info())
# print(ser3)
# print(ser3['Name'], ser3['Age'])
# print(ser3[0], ser3[1])



ser4 = np.random.randint(1, 100, (4, 4))
ser4 = pd.DataFrame(ser4)
print(ser4)

# print(lst2 / 100)

# print(lst + lst2)



#
# list = [rd.randrange(1, 100) for i in range(0, 100)]
# print(list)
#
# largest = list[0]
#
# for j in list:
#     if j > largest:
#         largest = j
#
# print(j)

