
#use of mode() function
# mode() function a sub-set of the statistics module
# We need to import statistics module before doing any work
import statistics
from statistics import mode
import numpy as np
#we import numpy as np


randnums = np.random.randint(0,21,15)
#create a variable names randnums and set it to np.random.rand
#here 0 is inclusive 21 is exclusive

print(randnums)
# Printing out the entire list
print("Most repeated value is:",statistics.mode(randnums))
# Printing out mode of given data-set
import numpy as np
from collections import Counter
from statistics import mode

array = np.random.randint(0,21,15)
print(array)
counts = np.bincount(array)
print (np.argmax(counts))