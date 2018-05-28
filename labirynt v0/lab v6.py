import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random as random

wymiar = 10
rozmiar = wymiar*2
lab = [[0]*(rozmiar+3) for i in range(rozmiar+3)]
######################################
fig, ax = plt.subplots()


print(random.triangular(0,np.pi,np.pi/2))


def przejscie(x, y):
        lab[x][y] = 2

        n = 0

        kierunki = []
        if lab[x + 2][y] == 1:
            kierunki.append(1)
        if lab[x - 2][y] == 1:
            kierunki.append(2)
        if lab[x][y + 2] == 1:
            kierunki.append(3)
        if lab[x][y - 2] == 1:
            kierunki.append(4)

        for i in range(1, rozmiar + 1, 2):
            for j in range(1, rozmiar + 1, 2):
                n = n + lab[i][j]

        if n == 0:
            return

        if len(kierunki) == 0:
            if droga[len(droga)-1] == 1:
                droga.pop()
                przejscie(x - 2, y)
            elif droga[len(droga)-1] == 2:
                droga.pop()
                przejscie(x + 2, y)
            elif droga[len(droga)-1] == 3:
                droga.pop()
                przejscie(x, y - 2)
            elif droga[len(droga)-1] == 4:
                droga.pop()
                przejscie(x, y + 2)
            elif droga[len(droga)-1] == 0:
                return

        if len(kierunki) == 0:
            return
        else:
            losowa = random.randint(0, len(kierunki)-1)

        if kierunki[losowa] == 1:
            lab[x + 1][y] = 2
            droga.append(1)
            przejscie(x + 2, y)
        elif kierunki[losowa] == 2:
            lab[x - 1][y] = 2
            droga.append(2)
            przejscie(x - 2, y)
        elif kierunki[losowa] == 3:
            lab[x][y + 1] = 2
            droga.append(3)
            przejscie(x, y + 2)
        elif kierunki[losowa] == 4:
            lab[x][y - 1] = 2
            droga.append(4)
            przejscie(x, y - 2)


def solve(x, y, f_x, f_y):
    lab[x][y] = 0

    kierunki = []
    if lab[x + 1][y] == 2:
        kierunki.append(1)
    if lab[x - 1][y] == 2:
        kierunki.append(2)
    if lab[x][y + 1] == 2:
        kierunki.append(3)
    if lab[x][y - 1] == 2:
        kierunki.append(4)

    if x == f_x and y == f_y:
        return

    if len(kierunki) == 0:
        if rozwiazanie[len(rozwiazanie) - 1] == 1:
            rozwiazanie.pop()
            solve(x - 2, y, f_x, f_y)
        elif rozwiazanie[len(rozwiazanie) - 1] == 2:
            rozwiazanie.pop()
            solve(x + 2, y, f_x, f_y)
        elif rozwiazanie[len(rozwiazanie) - 1] == 3:
            rozwiazanie.pop()
            solve(x, y - 2, f_x, f_y)
        elif rozwiazanie[len(rozwiazanie) - 1] == 4:
            rozwiazanie.pop()
            solve(x, y + 2, f_x, f_y)
        elif rozwiazanie[len(rozwiazanie) - 1] == 0:
            return

    if len(kierunki) == 0:
        return
    else:
        losowa = random.randint(0, len(kierunki) - 1)

    if kierunki[losowa] == 1:
        lab[x + 1][y] = 0
        rozwiazanie.append(1)
        solve(x + 2, y, f_x, f_y)
    elif kierunki[losowa] == 2:
        lab[x - 1][y] = 0
        rozwiazanie.append(2)
        solve(x - 2, y, f_x, f_y)
    elif kierunki[losowa] == 3:
        lab[x][y + 1] = 0
        rozwiazanie.append(3)
        solve(x, y + 2, f_x, f_y)
    elif kierunki[losowa] == 4:
        lab[x][y - 1] = 0
        rozwiazanie.append(4)
        solve(x, y - 2, f_x, f_y)

######################################

droga = []
droga.append(0)

rozwiazanie = []
rozwiazanie.append(0)

for i in range(0,rozmiar+1):
    for j in range(0,rozmiar+1):
        lab[i][j] = 1

wejscie = random.randrange(1, rozmiar, 2)
wyjscie = random.randrange(1, rozmiar, 2)

lab[0][wejscie] = 0
lab[rozmiar][wyjscie] = 0

przejscie(1, wejscie)

lab2 = lab

plt.plot([1, 0], [wejscie, wejscie], '-r')


for i in range(0, rozmiar+2, 2):
    for j in range(0, rozmiar+2, 2):
        if lab[i+1][j] == 1:
            plt.plot([i, i+2], [j, j], '-k')
        if lab[i][j+1] == 1:
            plt.plot([i, i], [j, j+2], '-k')


class tygrys(object):
    def __init__(self):
        self.alfa = random.randint(0, 3)
        self.x = round(random.randrange(1, rozmiar, 2), 1)
        self.y = round(random.randrange(1, rozmiar, 2), 1)
        self.age = 0.1
        if self.alfa == 0:
            self.next_point_y = self.y
            self.next_point_x = self.x + self.age
        if self.alfa == 1:
            self.next_point_y = self.y
            self.next_point_x = self.x - self.age
        if self.alfa == 2:
            self.next_point_y = self.y + self.age
            self.next_point_x = self.x
        if self.alfa == 3:
            self.next_point_y = self.y - self.age
            self.next_point_x = self.x



    def tygrys_move(self):
        #print(self.x,' ',self.y)

        if 0.99 < self.x % 2 < 1.01 and 0.99 < self.y % 2 < 1.01:
            a = int(self.x)
            if round(self.x) > a:
                a = int(self.x)+1
            b = int(self.y)
            if round(self.y) > b:
                b = int(self.y) + 1


            if lab2[a][b-1] != 1 and self.alfa == 0:
                self.y -= self.age
                self.alfa = 3
            if lab2[a][b+1] != 1 and self.alfa == 1:
                self.y += self.age
                self.alfa = 2
            if lab2[a+1][b] != 1 and self.alfa == 2:
                self.x += self.age
                self.alfa = 0
            if lab2[a-1][b] != 1 and self.alfa == 3:
                self.x -= self.age
                self.alfa = 1




tygrysy = []
x1 = []
y1 = []
n_x = []
n_y = []


for i in range(wymiar):
    tygrysy.append(tygrys())

for k in tygrysy:
    x1.append(k.x)
    y1.append(k.y)
    n_x.append(k.next_point_x)
    n_y.append(k.next_point_x)


line, = ax.plot(x1, y1, 'bo')


def animate(i):
    for k in range(wymiar):
        tygrysy[k].tygrys_move()
        x1[k] = tygrysy[k].x
        y1[k] = tygrysy[k].y
    line.set_data(x1, y1)
    return line,


def init():
    line.set_data([], [])
    return line,


ani = animation.FuncAnimation(fig, animate, frames=20, init_func=init,
                              interval=20, blit=True)

#####################################

solve(1, wejscie, rozmiar-1, wyjscie)
x = 1
y = wejscie

for i in range(0, len(rozwiazanie)):
        x_i = x
        y_i = y
        if rozwiazanie[i] == 1:
            x_i = x + 2
        elif rozwiazanie[i] == 2:
            x_i = x - 2
        elif rozwiazanie[i] == 3:
            y_i = y + 2
        elif rozwiazanie[i] == 4:
            y_i = y - 2

        plt.plot([x, x_i], [y, y_i], '-r')

        x = x_i
        y = y_i
plt.plot([x, x+1], [y, y], '-r')

####################################

plt.axis('off')
plt.show()
