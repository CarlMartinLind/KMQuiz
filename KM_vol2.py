from random import randint, sample
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
    vastusevalikud = []
    for k in sõnastik:
        vastusevalikud.append(k)
    
    if 'astakuks ' in vastusevalikud:
        sõna = 'definitsiooniga'
        failinimi = 'definitsioonid.txt'
    else:
        sõna = 'teoreemiga'
        failinimi = 'teoreemid.txt'
    
    koopia = vastusevalikud[:]
    õige = randint(0, len(vastusevalikud)-1)
    koopia.remove(vastusevalikud[õige])
    valed = sample(range(0, len(koopia)), 2)
    
    silt2 = Label(testiaken, text='Millise ' + sõna + ' on tegu?\n' + sõnastik[vastusevalikud[õige]])
    silt2.pack()
    vastuste_raam = Frame(testiaken)
    vastuste_raam.pack()
    v = StringVar()
    
    vastus1 = ttk.Radiobutton(testiaken, text=vastusevalikud[õige], variable=v, value=vastusevalikud[õige], command=lambda: vastuse_kontroll(vastusevalikud[õige], vastusevalikud[õige]))
    vastus2 = ttk.Radiobutton(testiaken, text=koopia[valed[0]], variable=v, value=koopia[valed[0]], command=lambda: vastuse_kontroll(koopia[valed[0]], vastusevalikud[õige]))
    vastus3 = ttk.Radiobutton(testiaken, text=koopia[valed[1]], variable=v, value=koopia[valed[1]], command=lambda: vastuse_kontroll(koopia[valed[1]], vastusevalikud[õige]))
    vastus1.pack()
    vastus2.pack()
    vastus3.pack()
    def topeltf():
        testiaken.destroy()
        küsi_küsimus(failist_sõnastik(failinimi))
    def vastuse_kontroll(valik, õige_vastus):
        if valik == õige_vastus:
            tagasiside = Label(testiaken, text='Suurepärane! Õige vastus!')
            tagasiside.pack()
        else:
            tagasiside = Label(testiaken, text='Peaaegu!!! Aga siiski mitte...')
            tagasiside.pack()
        edasi = Button(testiaken, text='Järgmine küsimus', command=lambda: topeltf())
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