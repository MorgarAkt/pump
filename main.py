import formatData
import ast
import matplotlib.pyplot as plt
import numpy as np
import polyFind as pf

x, y = formatData.formatdata()

x = ast.literal_eval(x)
y = ast.literal_eval(y)

x_refined = []
y_refined = []

for j in range(len(x)):
    if len(x) == 16:
        if j == 0 or j == 2 or j == 12:
            x_refined.append(x[j])
            y_refined.append(y[j])
    if len(x) == 12:
        if j == 0 or j == 2 or j == 10:
            x_refined.append(x[j])
            y_refined.append(y[j])


print("-----------------------------------------------------------")
print(x_refined)
print(y_refined)
print("-----------------------------------------------------------")


factor = 1.33729

x1 = np.linspace(0, x_refined[0][0]*factor, num=100)
fx1 = []

x2 = np.linspace(0, x_refined[1][0]*factor, num=100)
fx2 = []

x3 = np.linspace(0, x_refined[2][0]*factor, num=100)
fx3 = []

a1, b1 = pf.calcFomula(
x_refined[0][2], 
y_refined[0][2], 
x_refined[0][int((len(x_refined[0])-1)/2)], 
y_refined[0][int((len(x_refined[0])-1)/2)],
x_refined[0][-1],
y_refined[0][-1]
)
c1= y_refined[1][-1]*factor

a2, b2= pf.calcFomula(
x_refined[1][2], 
y_refined[1][2], 
x_refined[1][int((len(x_refined[0])-1)/2)], 
y_refined[1][int((len(x_refined[0])-1)/2)],
x_refined[1][-1],
y_refined[1][-1]
)
c2= y_refined[2][-1]*factor

a3, b3= pf.calcFomula(
x_refined[2][2], 
y_refined[2][2], 
x_refined[2][int((len(x_refined[0])-1)/2)], 
y_refined[2][int((len(x_refined[0])-1)/2)],
x_refined[2][-1],
y_refined[2][-1]
)
c3= y_refined[2][-1]*factor

function1= f"{a1}x^2 {b1}x {c1}"
function2= f"{a2}x^2 {b2}x {c2}"
function3= f"{a3}x^2 {b3}x {c3}"

for i in range(len(x1)):
    fx1.append((-0.00072*x1[i]**2 + 0.0723*x1[i] + 67.3)*factor)
    fx2.append((-0.004*x2[i]**2 + 1.10744*x2[i])*factor)
    fx3.append((-0.00088*x3[i]**2 + 0.057*x3[i] + 39.15)*factor)

print(function1)
print(function2)
print(function3)

plt.plot(x1, fx1)
plt.plot(x2, fx2)
plt.plot(x3, fx3)
plt.xlabel("X")
plt.xlabel("y")

plt.grid()
plt.axvline()
plt.axhline()
plt.savefig('my_plot.png')
plt.show()
