#Case6
# Elemanlarz 1 ile 17 arasındaki sayılardan oluşan 4*4 lük x matrisindeki cift sayıları
# boolean index ile alarak 2*4 lük y matrisini olusturalım


import numpy as np

x = np.arange (1, 17) . reshape (4,4)
print (x)
print()
y = x[x%2==0].reshape (2,4)
print (y)