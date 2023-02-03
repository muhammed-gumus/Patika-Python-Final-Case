#Case5
# [[0 1 2 3 4]
#  [5 6 7 8 9]
#  [10 11 12 13 14]
#  [15 16 17 18 19]
#  [20 21 22 23 24]] x matrisinden [[7 8]
#                                  [12 13]] y matrisini olusturunuz .

import numpy as np

x = np.arange (25).reshape (5,5)
print(x)
print()
y = x[1:3, 2:4]
print (y)
