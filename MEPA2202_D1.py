import numpy as np
import matplotlib.pyplot as plt

    ###############
    #### DEL 1 ####
    ###############

mass = 2300 # kg

## s ##
t = 0
dt = 0.0002
t_list = []
t_list.append(0)

## m ##
x = 0
x_1 = 1.5
x_list = []
x_list.append(x)

## m/s ##
v = 50 * 1e3/60**2
v_1 = 0
v_list = []
v_list.append(v)

## m/s2 ##
a = 0
a_list = []
a_list.append(a)

k = mass * (v**2)/(x_1**2)

while v > v_1:
    F = k*x
    ## F = ma -> a = F/m
    a = - F/mass
    a_list.append(a)

    ## Integrerer a for v
    v += a*dt
    v_list.append(v)

    ## Integrerer v for x
    x += v*dt
    x_list.append(x)

    t += dt
    t_list.append(t)
    #print(f'v={v_list}, x={x_list}')


a_max = abs(min(a_list))
F_max = abs(a_max)*mass

print(f'k = {round(k, 1)}')
print(f'a max = {round(a_max/9.81, 1)}g')
print(f'F max = {round(F_max * 1e-3)} kN')

plt.figure(figsize=(8, 10))

plt.subplot(3, 1, 1)
plt.plot(t_list, x_list)
plt.xlabel('Tid (s)')
plt.ylabel('Fjær kompresjon (m)')
plt.title('x(t)')
plt.grid()

plt.subplot(3, 1, 2)
plt.plot(t_list, v_list)
plt.xlabel('Tid (s)')
plt.ylabel('Fart (m/s)')
plt.title('v(t)')
plt.grid()

plt.subplot(3, 1, 3)
plt.plot(t_list, a_list)
plt.xlabel('Tid (s)')
plt.ylabel('Akselerasjon (m/s2)')
plt.title('a(t)')
plt.grid()

plt.tight_layout()
plt.show()
