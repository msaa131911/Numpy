import numpy as np
import pandas as pd

#numpy
arr=np.array([1,2,3,3,4,4,4,4,5])
ss=np.unique(arr)
print(ss)

#pandas
data = pd.Series(["Dhaka", "Chittagong", "Dhaka", "Khulna"])
print(data.unique())

#return_counts
values, counts = np.unique(arr, return_counts=True)
print(values,counts)

#এই ফাংশন ব্যবহার করা হয় দুইটি array-এর মধ্যে থাকা সব unique (অদ্বিতীয়) উপাদানকে একত্রে (union) করে একটি নতুন sorted array তৈরি করতে।
a = np.array([1, 2, 3, 4])
b = np.array([3, 4, 5, 6])

result = np.union1d(a, b)

print(result)

#এই ফাংশন ব্যবহার করা হয় দুইটি array-এর মধ্যে সাধারণ (common) উপাদানগুলো বের করতে।
result1 = np.intersect1d(a, b)

print(result1)

#এই ফাংশন ব্যবহার করা হয় দুইটি array-এর মধ্যে পার্থক্য (difference) বের করতে। 
#এটি সেই উপাদানগুলো বের করে যা প্রথম array-তে আছে কিন্তু দ্বিতীয় array-তে নেই।
set1 = np.array([1, 2, 3, 4])
set2 = np.array([3, 4, 5, 6])

newarr = np.setdiff1d(set1, set2, assume_unique=True)

print(newarr)

#দুই array-এর uncommon (অমিল) মানগুলো দেয়।
a1 = np.array([1, 2, 3, 4])
b1 = np.array([3, 4, 5, 6])

result2 = np.setxor1d(a1, b1)
print(result2)