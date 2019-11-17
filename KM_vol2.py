from random import randint, sample, shuffle
from tkinter import *
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import time
from threading import Timer


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
    testiaken.title('Kõrgema Matemaatika kordamistest')

    

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
    
    def kaota_tagasiside(labelName):
        labelName.destroy() 
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
            t = Timer(8.0, kaota_tagasiside, args=(tagasiside,))
            t.start()
        
            
            
        edasi = ttk.Button(testiaken, text='Järgmine küsimus', style="danger.TButton", command=lambda: uus_küsimus()).pack()
        lõpeta = ttk.Button(testiaken, text='Katkesta test', style="danger.TButton", command=lambda: testiaken.destroy()).pack()   
aken = ThemedTk(theme="radiance")
aken.title('Kõrgem Matemaatika I')
aken.geometry('300x200')

style = ttk.Style()
style.configure('winnative',font="arial 11")


silt1 = ttk.Label(aken, text='Vali küsimuste kategooria',font="arial 14").pack()

valik1= ttk.Button(aken, text='Teoreemid', style="danger.TButton", command=lambda: küsi_küsimus(failist_sõnastik('teoreemid.txt'))).pack()
#ttk.Button(aken, text="Styled Dangerously",style="danger.TButton").pack()
#style.map("new_state_new_stye.TButton",foreground=[("pressed","red"),("active","blue")])
valik2 = ttk.Button(aken, text='Definitsioonid', style="danger.TButton", command=lambda: küsi_küsimus(failist_sõnastik('definitsioonid.txt'))).pack()

def lopp1():
    aken.destroy()

def lopp2():
    silt3 = Label(aken, text='Aitäh, et küsimustele vastasid! Edu!')
    silt3.pack()
    sulge = ttk.Button(aken, text='Sulge programm', style="danger.TButton", command=lambda: lopp1()).pack()
    
lõpp = ttk.Button(aken, text='Lõpeta', style="danger.TButton", command=lambda: lopp2()).pack()

aken.mainloop()