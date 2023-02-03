#Case7
# Sinemaya giriş ücreti öğrenciler için 5TL, olmayanlar için 10TL. 100 kişi için 700 TL
# toplandığına göre öğrenci sayısı kactir

import numpy as np

price =  np.array ([[1, 1], [5,10]])
print(price)
unknown = np.array ([ 100, 700])
print(unknown)
result = np.linalg. solve (price, unknown)
print(result)