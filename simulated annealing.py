import math
import random
import numpy as np
import matplotlib.pyplot as plt
import copy


# define a distance function
def distance(route):
    tot_dis = 0
    for i in range(len(route)-1):
        dis = math.sqrt((route[i][0] - route[i+1][0])**2 + (route[i][1] - route[i+1][1])**2)
        tot_dis += dis
    return round(tot_dis,4)

# generate n pairs of coordinates for cities
num_cities = 30

cities = []
for i in range(num_cities):
    cities.append(tuple(random.sample(range(1,100), 2)))
# plot the city coordinates
plt.scatter(*zip(*cities))
plt.show()

# initialize a ramdomized route
init_route_order = [i for i in range(num_cities)]
random.shuffle(init_route_order)

# obtain the cities coordinates for the initial route
route = [cities[i] for i in init_route_order]

# plot the route by order of stopping by
plt.plot(*zip(*route),'-o')
plt.show()

init_route = route

# reset
route = init_route
print("the initial distance is {}".format(distance(route)))

# annealing starts
# logarithmic distribution

dis_progress = []

# try different activation functions
for iter in np.logspace(0, 3, num=100000)[::-1]:
#for iter in np.linspace(1, 100000, num=100000)[::-1]:
    i, j = sorted(random.sample(range(num_cities),2))
    new_route = route[:i] + [route[j]] + route[i+1:j] + [route[i]] + route[j+1:]

    if distance(new_route) < distance(route):
        route = copy.copy(new_route)
    elif (distance(new_route) > distance(route)
      and math.exp((distance(route) - distance(new_route))/iter) > random.random()):
        route = copy.copy(new_route)

    dis_progress.append(distance(route))

print("the final distance is {}".format(distance(route)))

plt.plot(dis_progress, '-o')
plt.show()

# plot optimized result
plt.plot(*zip(*route),'-o')
plt.show()
