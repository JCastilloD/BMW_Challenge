from ACOBMW import *
points = np.array((((5,5),(7,5)),((1,7),(3,7)),((4,4),(4,6)),((5,2),(7,2))))
#points = np.array((((5,6),(3,6)),((2,7),(2,5)),((2,5),(2,3)),((6,1),(6,3))))
Javs = BMWRoute(points)
eins, zwei ,Route= Javs.Start()


import matplotlib.pyplot as plt
x = []
y = []
for i in Route:
     x.append(i[0])
     y.append(i[1])

fig = plt.figure()
plt.plot(x,y)
plt.scatter(x,y, c = 'r', marker = 'o')
plt.grid()
