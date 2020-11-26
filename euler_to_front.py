#Programa para caulcular la ecuacion de Euler adelantada
import matplotlib.pyplot as plt
from sympy import exp
from numpy import array, zeros
h = 0.01
t = 0 
N=10
yi=5
y = zeros(N)
t = zeros(N)
#y[0] = 5
for i in range(N):
    
    DY = -20*yi + 7*exp(-0.5*t);
    y[i] = yi + (h*DY);
    t = t + h; 
    yi = y[i];
print(t)
print(y)
plt.plot(t,y)
