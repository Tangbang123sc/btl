# import pandas as pd
# import numpy as np
 
# df = pd.read_excel("DA\Financial Sample.xlsx")
# print(df.shape)
# print(df.info())
# print("hello")

import matplotlib.pyplot as plt
import numpy as np
data = np.random.normal(size=10000)
plt.hist(data, bins = 35)
plt.title('Histogram Example', fontsize = 14)
plt.show()