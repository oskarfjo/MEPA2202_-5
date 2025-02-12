import numpy as np
import matplotlib.pyplot as plt

    ###############
    #### OPP 2 ####
    ###############

dt = 0.02 # s

mass = 75 # kg
g = 9.81 # m/s2
Krb = 250 # N/m
Crb = 75 # Ns/m

direction_last = 1
t_last = 0

t = 0 # s
x = 0 # m
v = 0 # m/s

x_list = [0]
v_list = [0]
a_list = [-g]
t_list = [0]

vp = [0, 0]

def minmax(list):
    minimum = min(list)
    maksimum = max(list)
    if abs(minimum) > abs(maksimum):
        return minimum
    else:
        return maksimum

def drag(vel):
    if vel > 0: # sikkrer fortegn som motvirker hastighet
        sign = -1
    else:
        sign = 1
    C_d = 1.5
    area = 0.5 # m2
    rho = 1.225 # kg/m3 
    return sign * (C_d*area*rho)/2 * vel**2

while t < 20:

    if x < -10:
        Frb = Krb * (abs(x) - 10)
        Fdrb = - Crb * v
        F_s = Frb + Fdrb
    else:
        F_s = 0

    G = mass * (-g)

    F_sum = drag(v) + F_s + G

    ## F = ma _> a = F/m
    a = F_sum/mass

    v += a * dt
    x += v * dt

    t += dt

    direction = np.sign(abs(x) - abs(x_list[-1]))
    
    if direction != direction_last:
        vp.append(x)
        vp.pop(0)
        vp_dist = vp[-1] - vp[0]
        direction_last = direction
        if abs(vp_dist) <= 1:
            print(f'Tid til amplituden er mindre enn +- 0,5m = {round(t_last, 2)} s')
            print(f'Min og maks høyde er da [{round(vp[0], 2)}, {round(vp[1], 2)}]')
            break
        else:
            t_last = t

    x_list.append(x)
    v_list.append(v)
    a_list.append(a)
    t_list.append(t)

x_res = minmax(x_list)
v_res = minmax(v_list)
a_res = minmax(a_list)

print(f'Største hastighet = {round(v_res, 2)} m/s')
print(f'Største akselerasjon = {round(a_res, 2)} m/s2')
print(f'Største avstand fra platform = {abs(round(x_res, 2))} m')

zero_line = np.zeros(len(t_list))

plt.figure(figsize=(12, 12))

plt.subplot(3, 1, 1)
plt.plot(t_list, x_list)
plt.plot(t_list, zero_line, 'k-')
plt.xlabel('Tid (s)')
plt.ylabel('x(t)')
plt.title('Posisjon (m)')
plt.grid()

plt.subplot(3, 1, 2)
plt.plot(t_list, v_list)
plt.plot(t_list, zero_line, 'k-')
plt.xlabel('Tid (s)')
plt.ylabel('v(t)')
plt.title('Fart (m/s)')
plt.grid()

plt.subplot(3, 1, 3)
plt.plot(t_list, a_list)
plt.plot(t_list, zero_line, 'k-')
plt.xlabel('Tid (s)')
plt.ylabel('a(t)')
plt.title('Akselerasjon (m/s2)')
plt.grid()

plt.tight_layout()
plt.show()