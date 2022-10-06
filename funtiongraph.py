import numpy as np
import matplotlib.pyplot as plt

factor = 1.33729

x1 = np.linspace(0,240,num=100)
fx1 = []

x2 = np.linspace(0,204,num=100)
fx2 = []

x3 = np.linspace(0,205,num=100)
fx3 = []

a1 = 0
b1 = 0
c1 = 0

a2 = 0
b2 = 0
c2 = 0

a3 = 0
b3 = 0
c3 = 0

function1 = f"{a1}x^2 {b1}x {c1}"
function2 = f"{a2}x^2 {b2}x {c2}"
function3 = f"{a3}x^2 {b3}x {c3}"

for i in range(len(x1)):
    fx1.append((-0.00072*x1[i]**2 + 0.0723*x1[i] + 67.3)*factor)
    fx2.append((-0.004*x2[i]**2 + 1.10744*x2[i])*factor)
    fx3.append((-0.00088*x3[i]**2 + 0.057*x3[i] + 39.15)*factor)

print(function1)
print(function2)
print(function3)

plt.plot(x1,fx1)
plt.plot(x2,fx2)
plt.plot(x3,fx3)
plt.grid()
plt.axvline()
plt.axhline()
plt.savefig('my_plot.png')
plt.show()