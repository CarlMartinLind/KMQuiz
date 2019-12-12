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

# siia hakkavad tulema küsimused eraldi Labeli sisse, siis ei pea iga küsimuse jaoks uut akent avama
def ava_küsimuste_aken(failinimi):    
    küsimuste_aken = tk.Toplevel(aken)
    küsimuste_aken.title('Kõrgema matemaatika kordamistest')
    küsimuste_aken.geometry('600x360')
    
    küsimuste_raam = Frame(küsimuste_aken)
    küsimuste_raam.pack()
    
    nupu_raam = Frame(küsimuste_aken)
    nupu_raam.pack(pady=20)
    
    juhendi_silt = Label(nupu_raam, text = 'Test koosneb kümnest küsimusest. Alustamiseks vajuta nupule "Alusta".')
    juhendi_silt.pack()
    
    alusta = ttk.Button(nupu_raam, text='Alusta', style="danger.TButton", command=lambda: eemalda_nupp()).pack(pady=10)
    
    def eemalda_nupp():
        nupu_raam.destroy()
        küsi_küsimus(küsimustepagas)
    
    küsimustepagas = failist_sõnastik(failinimi)
# see funktsioon peaks suunama küsimuse küsimuste aknasse eraldi labeli sisse
    def küsi_küsimus(sõnastik, skoor = 0, kordi = 0):        
        if kordi == 10:
            küsimuste_aken.destroy()
            
            tagasisideaken = tk.Toplevel(aken)
            tagasisideaken.title('Kõrgema Matemaatika kordamistesti tagasiside')
            tagasisideaken.geometry('400x100')
        
            tagasisideraam = Frame(tagasisideaken)
            tagasisideraam.pack(pady=20)
        
            if skoor > 8:
                tekst = 'Kogusid ' + str(skoor) + ' punkti kümnest võimalikust. Suurepärane tulemus!'
            elif skoor > 5:
                tekst = 'Kogusid ' + str(skoor) + ' punkti kümnest võimalikust. Täitsa hästi!'
            elif skoor > 3:
                tekst = 'Kogusid ' + str(skoor) + ' punkti kümnest võimalikust. Polegi kõige hullem!'
            else:
                tekst = 'Kogusid ' + str(skoor) + ' punkti kümnest võimalikust.'
            
            tagasisidesilt = Label(tagasisideraam, text = tekst, wraplength=380)
            tagasisidesilt.pack()
            
            def sulge_aken():
                tagasisideaken.destroy()
            
            t = Timer(7.0, sulge_aken)
            t.start()
        
        else:
            küsimuste_raam = Frame(küsimuste_aken)
            küsimuste_raam.pack(pady=20)

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
                küsimus = 'Mis sobib lünka?'
            else:
                küsimus = 'Millise teoreemiga on tegu?'

#     testiaknasse Label, kuhu tuleb küsimus
            silt2 = Label(küsimuste_raam, text = str(kordi + 1) + '. ' + küsimus + '\n\n' + sõnastik[võtmed[õige]], wraplength=480)
            silt2.pack()
            

#     testiaknasse Frame, kuhu tulevad vastusevariandid
            vastuste_raam = Frame(küsimuste_raam)
            vastuste_raam.pack()
            
            valikusilt = Label(vastuste_raam)
            valikusilt.pack(pady=10)
            
            v = StringVar()
            ttk.Radiobutton(valikusilt, text=vastusevariandid[0], variable=v, value=vastusevariandid[0], command=lambda: vastuse_kontroll(vastusevariandid[0], võtmed[õige], skoor)).pack(anchor=W)
            ttk.Radiobutton(valikusilt, text=vastusevariandid[1], variable=v, value=vastusevariandid[1], command=lambda: vastuse_kontroll(vastusevariandid[1], võtmed[õige], skoor)).pack(anchor=W)
            ttk.Radiobutton(valikusilt, text=vastusevariandid[2], variable=v, value=vastusevariandid[2], command=lambda: vastuse_kontroll(vastusevariandid[2], võtmed[õige], skoor)).pack(anchor=W)
            ttk.Radiobutton(valikusilt, text=vastusevariandid[3], variable=v, value=vastusevariandid[3], command=lambda: vastuse_kontroll(vastusevariandid[3], võtmed[õige], skoor)).pack(anchor=W)
        
        
            def uus_küsimus(väärtus):
                küsimuste_raam.destroy()
                if väärtus == 'vale':
                    küsi_küsimus(küsimustepagas, skoor, kordi + 1)
                else:
                    küsi_küsimus(küsimustepagas, skoor + 1, kordi + 1)
        
            def vastuse_kontroll(valik, õige_vastus, skoor):

                for child in valikusilt.winfo_children():
                    child['state'] = 'disabled'
                
# et ei tuleks korduvaid küsimusi                
                del sõnastik[õige_vastus]
                
                if valik == õige_vastus:
                    väärtus = 'õige'
                    skoor += 1
                    tagasiside = Label(küsimuste_raam, text='Suurepärane! Õige vastus! Punkte hetkel: ' + str(skoor))
                    tagasiside.configure(bg="#2eff43")
                    tagasiside.pack()
                else:
                    väärtus = 'vale'
                    tagasiside = Label(küsimuste_raam, text='Peaaegu!!! Aga siiski mitte... Punkte hetkel: ' + str(skoor))
                    tagasiside.configure(bg="#ed8a72")
                    tagasiside.pack()
                
                if kordi == 9:
                    edasi_nupu_tekst = 'Lõpeta'
                else:
                    edasi_nupu_tekst = 'Järgmine küsimus'
                
                edasi = ttk.Button(küsimuste_raam, text = edasi_nupu_tekst, style="danger.TButton", command=lambda: uus_küsimus(väärtus)).pack(pady=5)
                lõpeta = ttk.Button(küsimuste_raam, text = 'Katkesta test', style="danger.TButton", command=lambda: küsimuste_aken.destroy()).pack()   


aken = ThemedTk(theme="radiance")
aken.title('Kõrgem Matemaatika I')
aken.geometry('350x220')

style = ttk.Style()
style.configure('winnative', font="arial 11")


silt1 = ttk.Label(aken, text='Vali küsimuste kategooria', font="arial 14").pack(pady=5)

valik1= ttk.Button(aken, text='Teoreemid', style="danger.TButton", command=lambda: ava_küsimuste_aken('teoreemid.txt')).pack()
valik2 = ttk.Button(aken, text='Definitsioonid', style="danger.TButton", command=lambda: ava_küsimuste_aken('definitsioonid.txt')).pack(pady=2)


def lopp1():
    aken.destroy()

def lopp2():
    silt3 = Label(aken, text='Aitäh, et küsimustele vastasid! Edukat eksamit!')
    silt3.pack()
    sulge = ttk.Button(aken, text='Sulge programm', style="danger.TButton", command=lambda: lopp1()).pack(pady=5)
    
lõpp = ttk.Button(aken, text='Lõpeta', style="danger.TButton", command=lambda: lopp2()).pack()

aken.mainloop()