#iclude files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("C:\Users\willa\My Drive\Schooling\Classes\USD\Spring 23\Probability and Statistics\Week 1\Income.dat", delimiter='\s+')

plt.hist(data['income'], bins=20)
plt.xlabel('Income')
plt.ylabel('Frequency')
plt.title('Histogram of Income Values')
plt.show()
print("Skewed right")