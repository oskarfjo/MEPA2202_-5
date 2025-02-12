import numpy as np
import matplotlib.pyplot as plt

    ###############
    #### DEL 2 ####
    ###############

## s ##
dt = 0.02
t_list = []
t = 0
t_list.append(0)


## fjær ##
spring_max = 1.5
spring_compression = 0
spring_compression_list = []
spring_compression_list.append(spring_compression)

## bil ##
mass_car = 1200
v_car = 50*1e3/60**2
a_car = 0
x_car = 0
x_car_list = []
v_car_list = []
a_car_list = []
x_car_list.append(x_car)
v_car_list.append(v_car)
a_car_list.append(a_car)

## objekt ##
mass_obj = 500
a_obj = 0
v_obj = 0
x_obj = 2
x_obj_list = []
v_obj_list = []
a_obj_list = []
x_obj_list.append(x_obj)
v_obj_list.append(v_obj)
a_obj_list.append(a_obj)

k = mass_car * ((50*1e3/60**2)**2)/((1.5)**2)

while t < 3:
    obj_car_distance = x_obj - x_car

    spring_compression = max(0, spring_max-obj_car_distance) # Fjærkraft hvis avstand = [0, 1.5m]

    ## F = k*x
    F = k*spring_compression

    ## F = ma -> a = F/m
    ## F er i mellom car og obj ; den virker neggativt på car og postivt på obj
    a_car = - F/mass_car
    a_obj = F/mass_obj

    ### Integrerer for v og x ###
    v_car += a_car*dt
    x_car += v_car*dt
    v_obj += a_obj*dt
    x_obj += v_obj*dt

    t += dt
    t_list.append(t)
    spring_compression_list.append(spring_compression)
    x_car_list.append(x_car)
    x_obj_list.append(x_obj)
    v_car_list.append(v_car)
    v_obj_list.append(v_obj)
    a_car_list.append(a_car)
    a_obj_list.append(a_obj)


print(f'Maksimal deformasjon av fjær = {round(max(spring_compression_list), 2)} m')
print(f'Maksimal akselerasjon av bil = {abs(round(min(a_car_list)/9.81, 2))}g')
print(f'Maksimal akselerasjon av objekt = {round(max(a_obj_list)/9.81, 2)}g')


plt.figure(figsize=(8, 14))

plt.subplot(4, 1, 1)
plt.plot(t_list, x_car_list, 'b-', label='Bil')
plt.plot(t_list, x_obj_list, 'r-', label='Objekt')
plt.xlabel('t - (s)')
plt.ylabel('x(t)')
plt.title('Posisjon (m)')
plt.legend()
plt.grid()

plt.subplot(4, 1, 2)
plt.plot(t_list, v_car_list, 'b-', label='Bil')
plt.plot(t_list, v_obj_list, 'r-', label='Objekt')
plt.xlabel('t - (s)')
plt.ylabel('v(t)')
plt.title('Fart (m/s)')
plt.legend()
plt.grid()

plt.subplot(4, 1, 3)
plt.plot(t_list, a_car_list, 'b-', label='Bil')
plt.plot(t_list, a_obj_list, 'r-', label='Objekt')
plt.xlabel('t - (s)')
plt.ylabel('a(t)')
plt.title('Akselerajson (m/s2)')
plt.legend()
plt.grid()

plt.subplot(4, 1, 4)
plt.plot(t_list, spring_compression_list, 'g-', label='Fjær kompresjon')
plt.xlabel('t - (s)')
plt.ylabel('x(t)')
plt.title('Fjær kompresjon (m)')
plt.grid()

plt.tight_layout()
plt.show()



##### KLADD #####

while False:
    obj_car_distance = x_obj - x_car
    print(obj_car_distance)
    if obj_car_distance <= 0:
        x_obj = x_car
        spring_compression = spring_max
    elif obj_car_distance <= spring_max:
        spring_compression = sat(obj_car_distance, 0, spring_max)
    else:
        spring_compression = 0

    if spring_compression > 0:
        a_car = (1/mass_car)*(-k * spring_compression)
    else:
        a_car = 0

    v_car += a_car*dt
    x_car += v_car*dt
    
    if spring_compression > 0:
        F = k * spring_compression
    else:
        F = 0

    a_obj = F/mass_obj
    v_obj += a_obj*dt
    x_obj += v_obj*dt

    t += dt
    t_list.append(t)
    spring_compression_list.append(spring_compression)
    x_car_list.append(x_car)
    x_obj_list.append(x_obj)
    v_car_list.append(v_car)
    v_obj_list.append(v_obj)
    a_car_list.append(a_car)
    a_obj_list.append(a_obj)