import numpy as np
import webbrowser
from tkinter import *

dds=np.zeros([2,3],dtype="int")
print(dds)
for i in range(dds.shape[0]):
    for j in range(dds.shape[1]):
        dds[i, j] = i + j
        
print("Modified array:")
print(dds)