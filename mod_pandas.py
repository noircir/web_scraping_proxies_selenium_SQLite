import pandas as pd

df = pd.read_csv("proxies_with_id.csv")
print(df.info())
print(df)

import matplotlib.pyplot as plt

fig, axes = plt.subplots(nrows = 1, ncols = 3, figsize = (16,4))
ax1, ax2 = fig.axes
ax1.hist(df['IP_address'], bins = 10, range = (0,1000)) # bin range = 1
ax1.set_title('IP address')
ax2.hist(df['Port'], bins = 10, range = (0,10000)) # bin range = 10
# ax2.set_title('Port')
# ax3.hist(df['Country_City'], bins = 10, range = (0,100), histtype = 'step')
# ax3.hist(movie_ratings['metascore'], bins = 10, range = (0,100), histtype = 'step')
# ax3.legend(loc = 'upper left')
# ax3.set_title('The Two Normalized Distributions')
for ax in fig.axes:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
plt.show()