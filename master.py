from random import *
from tkinter import *

lista_bomba = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

lista_polja = [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
               ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
               ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
               ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
               ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
               ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
               ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
               ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
               ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
               ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']]


def random_postavljanje(z, y):
    print('POSTAVLJAMO SE!')
    lista_zabrane = [z * 10 + y, z * 10 + y - 1, z * 10 + y + 1, (z + 1) * 10 + y, (z + 1) * 10 + y - 1,
                     (z + 1) * 10 + y + 1, (z - 1) * 10 + y, (z - 1) * 10 + y + 1, (z - 1) * 10 + y - 1]
    for i in range(23):
        prolaz = False
        while prolaz == False:
            random_i = randint(0, len(lista_bomba)-1)
            random_y = randint(0, len(lista_bomba[0])-1)
            spoj = random_i * 10 + random_y
            if lista_bomba[random_i][random_y] != 1 and spoj not in lista_zabrane:
                lista_bomba[random_i][random_y] = 1
                prolaz = True
    for i in lista_bomba:
        print(*i)


def provjera_bomba(i, y):
    brojac = 0
    if lista_bomba[i][y] == 1:
        return 'Poraz'
    if i > 0:
        if lista_bomba[i - 1][y] == 1:
            brojac += 1
        if y < 9:
            if lista_bomba[i - 1][y + 1] == 1:
                brojac += 1
        if y > 0:
            if lista_bomba[i - 1][y - 1] == 1:
                brojac += 1
    if i < 9:
        if lista_bomba[i + 1][y] == 1:
            brojac += 1
        if y > 0:
            if lista_bomba[i + 1][y - 1] == 1:
                brojac += 1
        if y < 9:
            if lista_bomba[i + 1][y + 1] == 1:
                brojac += 1
    if y < 9:
        if lista_bomba[i][y + 1] == 1:
            brojac += 1
    if y > 0:
        if lista_bomba[i][y - 1] == 1:
            brojac += 1
    return brojac


def nista(event):
    return


def zastavica(i, y):
    boja=lista_polja[i][y].cget('bg')
    if boja == 'grey':
        lista_polja[i][y].config(bg='red', state=DISABLED)
    else:
        lista_polja[i][y].config(bg='grey', state=NORMAL)


def clear():
    L = root.place_slaves()
    for i in range(len(L)):
        L[i].destroy()


def ciscenje_polja(i, y):
    global prvi_klik
    if prvi_klik:
        random_postavljanje(i, y)
        prvi_klik = False
    if provjera_bomba(i, y) == 0 and lista_bomba[i][y] != 'P':
        lista_bomba[i][y] = 'P'
        lista_polja[i][y].config(bg='white', state=DISABLED, borderwidth=5)
        lista_polja[i][y].bind('<Button-3>', nista)
        if i > 0:
            ciscenje_polja(i - 1, y)
            if y < 9:
                ciscenje_polja(i - 1, y + 1)
            if y > 0:
                ciscenje_polja(i - 1, y - 1)
        if i < 9:
            ciscenje_polja(i + 1, y)
            if y > 0:
                ciscenje_polja(i + 1, y - 1)
            if y < 9:
                ciscenje_polja(i + 1, y + 1)
        if y < 9:
            ciscenje_polja(i, y + 1)
        if y > 0:
            ciscenje_polja(i, y - 1)
    elif lista_bomba[i][y] == 1:
        for x in range(len(lista_bomba)):
            for z in range(len(lista_bomba[x])):
                if lista_bomba[x][z] == 1:
                    lista_polja[x][z].config(bg='red')
                if lista_polja[x][z].cget('bg') == 'red' and lista_bomba[x][z] != 1:
                    lista_polja[x][z].config(bg='green', text='Ups')
        for x in range(len(lista_polja)):
            for z in range(len(lista_polja[x])):
                lista_bomba[x][z] = 0
                lista_polja[x][z].config(command=start, state=NORMAL)
                lista_polja[x][z].bind('<Button-3>', nista)
        for h in lista_bomba:
            print(*h)
    elif lista_bomba[i][y] != 'P':
        lista_polja[i][y].config(text=provjera_bomba(i, y), bg='light blue', state=DISABLED, borderwidth=5)
        lista_polja[i][y].bind('<Button-3>', nista)
        lista_bomba[i][y] = 'P'
    pobjeda = True
    for z in lista_bomba:
        if 0 in z:
            pobjeda = False
    if pobjeda == True:
        print('Bravo! Pobjedio si.')
        for i in range(len(lista_polja)):
            for y in range(len(lista_polja[i])):
                lista_polja[i][y].config(command=start)
                lista_polja[i][y].bind('<Button-3>', nista)

root = Tk()
prvi_klik = True
boja = True
def start():
    clear()
    global prvi_klik
    prvi_klik = True
    for i in range(len(lista_polja)):
        for y in range(len(lista_polja[i])):
            lista_polja[i][y] = Button(root, width=3, height=1, bg='grey', command=lambda x=i, z=y: ciscenje_polja(x, z),
                                       borderwidth=5)
            lista_polja[i][y].bind('<Button-3>', lambda event, x=i, z=y: zastavica(x, z))
            lista_polja[i][y].grid(row=i, column=y)
start()

'''
for i in range(len(lista_polja)):
    print(i, '|', *lista_polja[i])
global prekid
prekid = False
prvi_klik = True
while not prekid:
    pobjeda = True
    iy = input('Unesite koordinate polja kojeg želite odabrati(yx): ')
    if len(iy) == 0: 
        print('Molim unesite validan unos (0 - 99)')
        continue
    if int(iy) > 99 or int(iy) < 0:
        print('Molim unesite validan unos (0 - 99)')
        continue
    kord_i = int(iy[0])
    kord_y = int(iy[1])
    if prvi_klik:
        random_postavljanje(kord_i, kord_y)
        prvi_klik = False
    if lista_polja[kord_i][kord_y] != '.':
        print('Molim unesite koordinate polja koje nije već provjereno!')
    elif provjera_bomba(kord_i, kord_y) == 'Poraz':
        prekid = True
        print('BOOM, izgubio si!')
    else:
        ciscenje_polja(kord_i, kord_y)
        L = ['   ',0,1,2,3,4,5,6,7,8,9]
        print(*L)
        for i in range (len(lista_polja)):
            print(i, '|', *lista_polja[i])
    for u in lista_bomba:
        if '0' in u:
            pobjeda = False
    if pobjeda:
        print('Pobjedio si!')
        prekid = True
'''

root.mainloop()
