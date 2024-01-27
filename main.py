import matplotlib.pyplot as plt  
import numpy as np

animals=np.array(['dog','cat','lion','elephant','tiger'])
frequency=np.array([20,30,10,54,23])
labels=np.array(['red','blue','green','orange','yellow'])
color=np.array(['red','blue','green','orange','yellow'])

plt.bar(animals,frequency,label=labels,color=color)
plt.legend(title="Animals Color")

plt.savefig('bars.png')

# fig,ax=plt.subplots()
# fruits = ['apple', 'blueberry', 'cherry', 'orange']
# counts = [40, 100, 30, 55]
# bar_labels = ['red', 'blue', 'yellow', 'orange']
# bar_colors = ['tab:red', 'blue', 'red', 'orange']

# ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

# ax.set_ylabel('fruit supply')
# ax.set_title('Fruit supply by kind and color')
# ax.legend(title='Fruit color')

# plt.savefig('bars.png', bbox_inches='tight')