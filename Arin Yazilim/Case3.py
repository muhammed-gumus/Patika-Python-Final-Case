#Case3
# 1 ile 10 arasnda rastgele 16 elemandan olusan 4*4 lük bit matris oluşturunuz

import numpy as np

x = np.random.randint(1, 10, 16).reshape(4,4)
print(x)