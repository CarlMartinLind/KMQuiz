from random import randint, sample, shuffle
from tkinter import *
import tkinter as tk
from tkinter import ttk


def failist_sõnastik(failinimi):
    f = open(failinimi, encoding='UTF-8')
    küs_vas = {}
    for rida in f:
        a = rida.strip().split(';')
        küs_vas[a[0]] = a[1]
    f.close()
    return küs_vas

def küsi_küsimus(sõnastik):
    testiaken = tk.Toplevel(aken)
    testiaken.title('Test')

#    siin saab järjendi (vastusevariandid), kus on 4 vastusevarianti, millest kolm on valed ja üks õige. 
    võtmed = []
    for k in sõnastik:
        võtmed.append(k)
    koopia = võtmed[:]
    õige = randint(0, len(võtmed)-1)
    koopia.remove(võtmed[õige])
    valed = sample(range(0, len(koopia)), 3)
    vastusevariandid = []
    vastusevariandid.append(võtmed[õige])
    for i in range(3):
        vastusevariandid.append(koopia[valed[i]])
    shuffle(vastusevariandid)

#     sõna on vaja silt2 loomisel ja failinime, kui peaks küsimuste kategooriat vahetatama (funktsioonis uus_küsimus())
    if 'astakuks ' in võtmed:
        sõna = 'definitsiooniga'
        failinimi = 'definitsioonid.txt'
    else:
        sõna = 'teoreemiga'
        failinimi = 'teoreemid.txt'

#     testiaknasse Label, kuhu tuleb küsimus
    silt2 = Label(testiaken, text='Millise ' + sõna + ' on tegu?\n' + sõnastik[võtmed[õige]])
    silt2.pack()

#     testiaknasse Frame, kuhu tulevad vastusevariandid. Proovisin valikunuppe tekitada ka tsükliga, aga siis vastuste kontrollimine ei olnud õige
    vastuste_raam = Frame(testiaken)
    vastuste_raam.pack()
    v = StringVar()
    ttk.Radiobutton(testiaken, text=vastusevariandid[0], variable=v, value=vastusevariandid[0], command=lambda: vastuse_kontroll(vastusevariandid[0], võtmed[õige])).pack()
    ttk.Radiobutton(testiaken, text=vastusevariandid[1], variable=v, value=vastusevariandid[1], command=lambda: vastuse_kontroll(vastusevariandid[1], võtmed[õige])).pack()
    ttk.Radiobutton(testiaken, text=vastusevariandid[2], variable=v, value=vastusevariandid[2], command=lambda: vastuse_kontroll(vastusevariandid[2], võtmed[õige])).pack()
    ttk.Radiobutton(testiaken, text=vastusevariandid[3], variable=v, value=vastusevariandid[3], command=lambda: vastuse_kontroll(vastusevariandid[3], võtmed[õige])).pack()

    def uus_küsimus():
        testiaken.destroy()
        küsi_küsimus(failist_sõnastik(failinimi))
    def vastuse_kontroll(valik, õige_vastus):
        if valik == õige_vastus:
            tagasiside = Label(testiaken, text='Suurepärane! Õige vastus!')
            tagasiside.pack()
        else:
            tagasiside = Label(testiaken, text='Peaaegu!!! Aga siiski mitte...')
            tagasiside.pack()
        edasi = Button(testiaken, text='Järgmine küsimus', command=lambda: uus_küsimus())
        edasi.pack()
        lõpeta = Button(testiaken, text='Aitab sellest testist', command=lambda: testiaken.destroy())
        lõpeta.pack()
    
aken = Tk()
aken.title('KM testid')
aken.geometry('300x200')

silt1 = Label(aken, text='Vali küsimuste kategooria')
silt1.pack()

valik1 = Button(aken, text='Teoreemid', command=lambda: küsi_küsimus(failist_sõnastik('teoreemid.txt')))
valik1.pack()
valik2 = Button(aken, text='Definitsioonid', command=lambda: küsi_küsimus(failist_sõnastik('definitsioonid.txt')))
valik2.pack()

def lopp1():
    aken.destroy()

def lopp2():
    silt3 = Label(aken, text='Aitäh, et küsimustele vastasid! Edu!')
    silt3.pack()
    sulge = Button(aken, text='Sulge programm', command=lambda: lopp1())
    sulge.pack()
    
lõpp = Button(aken, text='Lõpeta', command=lambda: lopp2())
lõpp.pack()

aken.mainloop()