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

root = Tk()
prvi_klik = True
boja = True
font = 'Fixedsys 20'
broj_zastavica = 15
broj_1 = PhotoImage(file='jedan.png')
broj_2 = PhotoImage(file='dva.png')
broj_3 = PhotoImage(file='tri.png')
broj_4 = PhotoImage(file='cetiri.png')
broj_5 = PhotoImage(file='pet.png')
broj_6 = PhotoImage(file='sest.png')
virus = PhotoImage(file='corona.png')
obicno = PhotoImage(file='proba.png')
rjeseno = PhotoImage(file='rjeseno.png')
zastavica_slika = PhotoImage(file='zastavica.png')
pogresno = PhotoImage(file='pogresno.png')
dezinficijens= PhotoImage(file='hint.png')

def random_postavljanje(z, y):
    print('POSTAVLJAMO SE!')
    lista_zabrane = [z * 10 + y, z * 10 + y - 1, z * 10 + y + 1, (z + 1) * 10 + y, (z + 1) * 10 + y - 1,
                     (z + 1) * 10 + y + 1, (z - 1) * 10 + y, (z - 1) * 10 + y + 1, (z - 1) * 10 + y - 1]
    for i in range(15):
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


def provjera_bomba(i, y, vrsta, polje):
    lista=['žnj', broj_1, broj_2, broj_3, broj_4, broj_5, broj_6]
    global slika_polja
    brojac = 0
    hint_potvrda = False
    if lista_bomba[i][y] == vrsta:
        return 'Poraz'
    if i > 0:
        if lista_bomba[i - 1][y] == vrsta:
            hint_potvrda = True
            brojac += 1
        if y < 9:
            if lista_bomba[i - 1][y + 1] == vrsta:
                hint_potvrda = True
                brojac += 1
        if y > 0:
            if lista_bomba[i - 1][y - 1] == vrsta:
                hint_potvrda = True
                brojac += 1
    if i < 9:
        if lista_bomba[i + 1][y] == vrsta:
            hint_potvrda = True
            brojac += 1
        if y > 0:
            if lista_bomba[i + 1][y - 1] == vrsta:
                hint_potvrda = True
                brojac += 1
        if y < 9:
            if lista_bomba[i + 1][y + 1] == vrsta:
                hint_potvrda = True
                brojac += 1
    if y < 9:
        if lista_bomba[i][y + 1] == vrsta:
            hint_potvrda = True
            brojac += 1
    if y > 0:
        if lista_bomba[i][y - 1] == vrsta:
            hint_potvrda = True
            brojac += 1
    if vrsta == 'P':
        return hint_potvrda
    elif polje:
        slika_polja=lista[brojac]
        return slika_polja
    else:
        return brojac

def nista(event):
    return


def zastavica(i, y):
    global zastavica_l
    global broj_zastavica
    boja=lista_polja[i][y].cget('bg')
    if boja == 'grey':
        lista_polja[i][y].config(bg='red', image=zastavica_slika)
        lista_polja[i][y].bind('<Button-1>', nista)
        broj_zastavica += -1
        zastavica_l.config(text=broj_zastavica)
    else:
        lista_polja[i][y].config(bg='grey', image=obicno)
        lista_polja[i][y].bind('<Button-1>', lambda event, x=i, z=y: ciscenje_polja(x, z))
        broj_zastavica += 1
        zastavica_l.config(text=broj_zastavica)


def clear():
    L = root.place_slaves()
    for i in range(len(L)):
        L[i].destroy()


def ciscenje_polja(i, y):
    global prvi_klik
    if prvi_klik:
        random_postavljanje(i, y)
        prvi_klik = False
    if provjera_bomba(i, y, 1, False) == 0 and lista_bomba[i][y] != 'P':
        lista_bomba[i][y] = 'P'
        lista_polja[i][y].config(bg='grey', image=rjeseno, relief='sunken', borderwidth=2)
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
                    lista_polja[x][z].config(bg='red', image=virus)
                if lista_polja[x][z].cget('bg') == 'red' and lista_bomba[x][z] != 1:
                    lista_polja[x][z].config(bg='red', image=pogresno)
        for x in range(len(lista_polja)):
            for z in range(len(lista_polja[x])):
                lista_bomba[x][z] = 0
                lista_polja[x][z].bind('<Button-1>', lambda event: start())
                lista_polja[x][z].bind('<Button-3>', nista)
        for h in lista_bomba:
            print(*h)
    elif lista_bomba[i][y] != 'P':
        lista_polja[i][y].config(image=provjera_bomba(i, y, 1, True), bg='grey', relief='sunken', borderwidth=2)
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
                if lista_bomba[i][y] == 1:
                    lista_polja[i][y].config(image=zastavica_slika)
                lista_polja[i][y].bind('<Button-1>', lambda event: start())
                lista_polja[i][y].bind('<Button-3>', nista)


def start():
    for i in lista_polja:
        for y in i:
            y = ''
    for i in lista_bomba:
        for y in i:
            y = 0
    clear()
    global prvi_klik
    prvi_klik = True
    hint_gumb = Label(root, width=4, height=1, font=font, borderwidth=2, text='Hint', relief="raised")
    hint_gumb.grid(row=0, column=0, columnspan=2)
    hint_gumb.bind('<Button-1>', lambda event: hint())
    global zastavica_l
    zastavica_l = Label(root, width=4, height=1, font=font, borderwidth=2, text=broj_zastavica, relief="raised", fg='dark red')
    zastavica_l.grid(row=0, column=3, columnspan=2)
    for i in range(len(lista_polja)):
        for y in range(len(lista_polja[i])):
            lista_polja[i][y] = Label(root, image=obicno, bg='grey', borderwidth=2, relief="raised")
            lista_polja[i][y].bind('<Button-1>', lambda event, x=i, z=y: ciscenje_polja(x, z))
            lista_polja[i][y].bind('<Button-3>', lambda event, x=i, z=y: zastavica(x, z))
            lista_polja[i][y].grid(row=i+1, column=y)

L = []
def hint():
    for z in range (len(lista_bomba)):
        for h in range (len(lista_bomba[z])):
            if lista_bomba[z][h] == 0 and provjera_bomba(z, h, 'P', False):
                lista_polja[z][h].config(image=dezinficijens)
                return







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
