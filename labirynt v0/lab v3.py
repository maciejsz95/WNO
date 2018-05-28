import matplotlib.pyplot as plt
import random

wymiar = 10
rozmiar = wymiar*2
lab = [[0]*(rozmiar+3) for i in range(rozmiar+3)]

droga = []
droga.append(0)

rozwiazanie = []
rozwiazanie.append(0)

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
    lab[x][y] = 1

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
        lab[x + 1][y] = 1
        rozwiazanie.append(1)
        solve(x + 2, y, f_x, f_y)
    elif kierunki[losowa] == 2:
        lab[x - 1][y] = 1
        rozwiazanie.append(2)
        solve(x - 2, y, f_x, f_y)
    elif kierunki[losowa] == 3:
        lab[x][y + 1] = 1
        rozwiazanie.append(3)
        solve(x, y + 2, f_x, f_y)
    elif kierunki[losowa] == 4:
        lab[x][y - 1] = 1
        rozwiazanie.append(4)
        solve(x, y - 2, f_x, f_y)


for i in range(0,rozmiar+1):
    for j in range(0,rozmiar+1):
        lab[i][j] = 1

wejscie = random.randrange(1, rozmiar, 2)
wyjscie = random.randrange(1, rozmiar, 2)

lab[0][wejscie] = 0
lab[rozmiar][wyjscie] = 0

przejscie(1, wejscie)

plt.plot([1, 0], [wejscie, wejscie], '-r')


for i in range(0, rozmiar+2, 2):
    for j in range(0, rozmiar+2, 2):
        if lab[i+1][j] == 1:
            plt.plot([i, i+2], [j, j], '-k')
        if lab[i][j+1] == 1:
            plt.plot([i, i], [j, j+2], '-k')

for p in range(0, wymiar):
    tygrysy_x = random.randrange(1, rozmiar, 2)
    tygrysy_y = random.randrange(1, rozmiar, 2)
    plt.plot(tygrysy_x, tygrysy_y, "bo")

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

plt.axis('off')

plt.show()
