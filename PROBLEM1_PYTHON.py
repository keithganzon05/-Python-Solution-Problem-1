import numpy as np
import matplotlib.pyplot as plt
condition = 0 
integer = 99

while condition == 0:
    if integer <= 9:
        array = np.empty(integer, dtype=np.int)
        array2 =np.empty(integer, dtype=np.int)
        for n in range(integer):
            array[n] = ((n*n)-7)
            array2[n]= integer
            integer = integer-1
            print (array[n])
        array2 = np.sort(array2)
        condition = 1        
    else:
        while integer>=10:
            integer = integer-10
            condition = 0         
plt.stem(array2, array, use_line_collection=True)