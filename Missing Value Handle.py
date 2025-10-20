import numpy as np

# কিছু missing value সহ array
arr = np.array([1, 2, np.nan, 4, np.nan, 6])

# 🔍 Missing value (NaN) খুঁজে বের করা
print(np.isnan(arr))  
# [False False  True False  True False]

# ❌ Missing value বাদ দেওয়া
clean_arr = arr[~np.isnan(arr)]
print(clean_arr)
# [1. 2. 4. 6.]

# ✅ Missing value replace করা (যেমন: 0 দিয়ে)
filled_arr = np.nan_to_num(arr, nan=0)
print(filled_arr)
# [1. 2. 0. 4. 0. 6.]