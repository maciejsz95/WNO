import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random as random
from scipy.spatial import ConvexHull

#jclass point(object):

class tygrys(object):
     def __init__(self):
         self.x = random.uniform(0, 6)
         self.y = random.uniform(0, 6)
         self.alfa= random.uniform(0, np.pi*2)
         self.age = random.uniform(0,0.1)
         self.vage =[self.alfa+ np.pi/2, self.alfa-np.pi/2]
         self.next_point_x= self.x + self.age*np.cos(self.alfa)
         self.next_point_y= self.y + self.age*np.sin(self.alfa)


     def tygrys_move(self):
         if self.x == 6:
            self.x -= 1
         elif self.x == 0:
             self.x += 1

         if self.y ==6:
            self.y -= 1
         elif self.y ==0:
             self.y += 1

     def vector(self):
         return [self.age*np.cos(self.alfa),self.age*np.sin(self.alfa)]



# class tigers_group(tygrys):
#
#     def _init_(self,number):
#
#         for i in range(number):
#             self.tigers.append(tygrys.__init__(self))
#
#
#     def get_x_positions(self):
#         return np.concatenate([[tiger.x for tiger in self.tigers],[tiger.y for tiger in self.tigers]])
#     # def get_y_positions(self):
#     #     return [tiger.y for tiger in self.tigers]
#     def get_alfa(self):
#         return [tiger.alfa for tiger in self.tigers]
#     def get_next_positions(self):
#         return np.concatenate([[tiger.next_point_x for tiger in self.tigers],[tiger.next_point_y for tiger in self.tigers]])
#

tygrysy=[]
x=[]
y=[]
n_x=[]
n_y=[]

for i in range(10):
    tygrysy.append(tygrys())

for k in tygrysy:
    x.append(k.x)
    y.append(k.y)
    n_x.append(k.next_point_x)
    n_y.append(k.next_point_x)


##############################################

# tygrysy = tigers_group(10)
# positions = tygrysy.get_x_positions()
# print( positions)
#[K,V] = ConvexHull(x,y)
fig, ax = plt.subplots()
#hull =ConvexHull([x,y])
line,=ax.plot(x , y,'k*')
#vector=ax.plot()



def animate(i):

    for k in range(10):
        tygrysy[k].tygrys_move()
        x[k]=tygrysy[k].x
        y[k]=tygrysy[k].y
    line.set_data(x,y)
    return line,


def init():
    line.set_data([],[])
    return line,

ani = animation.FuncAnimation(fig, animate, frames=1000, init_func=init,
                              interval=25, blit=True)
plt.show()
#####################################



#print (x)
#plt.plot(x,y