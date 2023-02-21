#include files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = "C:/Users/willa/My Drive/Schooling/Classes/USD/Spring 23/Probability and Statistics/Week 1/Income.dat"
data = pd.read_csv(url, delimiter='\s+')

"""
testing a different commit method"""

plt.hist(data['income'], bins=20)
plt.xlabel('Income')
plt.ylabel('Frequency')
plt.title('Histogram of Income Values')
plt.show()
print("Skewed right")