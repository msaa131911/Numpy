import numpy as np


arr = np.array([1, 2, np.nan, 4, np.nan, 6])


print(np.isnan(arr))  
# [False False  True False  True False]


clean_arr = arr[~np.isnan(arr)]
print(clean_arr)


#Missing value replace করা=0
filled_arr = np.nan_to_num(arr, nan=0)
print(filled_arr)
