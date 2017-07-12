# basic plotting
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [3, 2, 9, 5]
plt.plot(x, y, 'o:', color='teal')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('a basic plot')
plt.show()