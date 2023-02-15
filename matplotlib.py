import matplotlib 
import pyplot as plt
# definindo o backend do matplotlib no arquivo jupyter
plt.figure(figsize=(9,6), dpi=75)
x = [1,6,10]
y = [5,13,27]

plt.plot(x,y)
plt.show()
plt.draw()
