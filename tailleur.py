from tkinter import*
from time import strftime
import tkinter.messagebox
import mysql.connector as sql
base=sql.connect(
    host='localhost',
    username='root',
    passwd='12345678',
    database='Louise_ceb')
curseur=base.cursor()

fen=Tk()
fen.geometry('1200x800+50+70')
fen.title('DressMakerHouse DMH')
fen.config(bg='gray25')

lbl_p=Label(fen,text='COUTURE ETRNEL BENIT',font=('',16,'bold'),fg='white',bg='gray25')
lbl_p.place(x=343,y=40)
#=================================Boite 1===========================================
canvas=Canvas(fen,bg='#E67E30',width=300,height=750)

#=================================variable==========================================
char1=StringVar()
char2=StringVar()
char3=StringVar()
char4=StringVar()
char5=StringVar()
char6=StringVar()

entier1=DoubleVar()
entier2=DoubleVar()
entier3=DoubleVar()
entier4=DoubleVar()
entier5=DoubleVar()
entier6=DoubleVar()
entier7=DoubleVar()
entier8=DoubleVar()
entier9=DoubleVar()
entier10=DoubleVar()
entier11=DoubleVar()
entier12=DoubleVar()
entier13=DoubleVar()
entier14=DoubleVar()
entier15=DoubleVar()
entier16=DoubleVar()
entier17=DoubleVar()
entier18=DoubleVar()
entier18=DoubleVar()
entier19=DoubleVar()
entier20=DoubleVar()
entier21=DoubleVar()
entier22=DoubleVar()

dos=DoubleVar()
epaul=DoubleVar()
epaul_manche=DoubleVar()
poitrine=DoubleVar()
taille=DoubleVar()
long_taille=DoubleVar()
bassin=DoubleVar()
lmanche=DoubleVar()
tmanche=DoubleVar()
pince=DoubleVar()
long_total=DoubleVar()
lrobe=DoubleVar()
ceinture=DoubleVar()
cuisse=DoubleVar()
genoux=DoubleVar()
long_jupe=DoubleVar()
modele=StringVar()

nom_client=StringVar()
prenom_client=StringVar()
tel_client=IntVar()
adresse=StringVar()

nom_charge=StringVar()
prenom_charge=StringVar()
tel_charge=IntVar()

date=StringVar()
listes=[]

#================================ Date =============================================
Date=strftime("%Y-%m-%d")
#================================ Déclaration des fonctions pour les boutons =======
class DMH:
    def __init__(self,nom_client,prenom_client,tel_client,adresse,nom_charge,prenom_charge,tel_charge,\
                dos,epaul,epaul_manche,poitrine,taille,long_taille,bassin,lmanche,tmanche,pince,long_total,lrobe,\
                ceinture,cuisse,genoux,long_jupe,modele,retrait):
                self.nom_client=nom_client,
                self.prenom_client=prenom_client,
                self.tel_client=tel_client,
                self.adresse=adresse,

                self.nom_charge=nom_charge,
                self.prenom_charge=prenom_charge,
                self.tel_charge=tel_charge,
                
                self.dos=dos,
                self.epaul=epaul,
                self.epaul_manche=epaul_manche,
                self.poitrine=poitrine,
                self.taille=taille,
                self.long_taille=long_taille,
                self.bassin=bassin,
                self.lmanche=lmanche,
                self.tmanche=tmanche,
                self.pince=pince,
                self.long_total=long_total,
                self.lrobe=lrobe,
                self.ceinture=ceinture,
                self.cuisse=cuisse,
                self.genoux=genoux,
                self.long_jupe=long_jupe,
                self.modele=modele
                self.retrait=retrait
    
    def __eq__(self, other):
        return(self.nom_charge==other.nom_charge and self.prenom_charge==other.prenom_charge and self.tel_charge==other.tel_charge and \
                self.nom_client==other.nom_client and self.prenom_client==other.prenom_client and self.tel_client==other.tel_client and \
                self.adresse==other.adresse and self.dos==other.dos and self.epaul==other.epaul and self.epaul_manche==other.epaul_manche and\
                self.poitrine==other.poitrine and self.taille==other.taille and self.long_taille==other.long_taille and self.bassin==other.bassin and\
                self.lmanche==other.lmanche and self.tmanche==other.tmanche and self.pince==other.pince and self.long_total==other.long_total and\
                self.lrobe==other.lrobe and self.ceinture==other.ceinture and self.cuisse==other.cuisse and self.genoux==other.genoux and\
                self.long_jupe==other.long_jupe and self.modele==other.modele and self.retrait==other.retrait)

def appartient(liste,val):
    for i in range(len(liste)):
        if liste[i].__eq__(val):
            return TRUE
    return FALSE

def iExit():
    iExit = tkinter.messagebox.askyesno("Quitter", "Êtes-vous sûr de quitter?")
    if iExit>0:
        fen.destroy()
        return

def valider():
    global listes
    if entry_nom_client.get() and entry_prenom_client.get() and entry_tel_client.get() and entry_adresse.get() and \
    entry_nom_charge.get()and entry_prenom_charge.get()and entry_tel_charge.get() and entry_dos.get() and entry_epaul.get() and\
    entry_epaul_manche.get() and entry_poitrine.get() and entry_taille.get() and entry_long_taille.get() and entry_bassin.get() and\
    entry_lmanche.get() and entry_tmanche.get() and entry_pince.get() and entry_long_total.get() and entry_lrobe.get() and\
    entry_ceinture.get() and entry_cuisse.get() and entry_genoux.get() and entry_long_jupe.get() and entry_modele.get() and entry_retrait.get():
        pn=DMH(entry_nom_client.get(),entry_prenom_client.get(),entry_tel_client.get(),entry_adresse.get(),\
        entry_nom_charge.get(),entry_prenom_charge.get(),entry_tel_charge.get(),entry_dos.get(), entry_epaul.get(),\
        entry_epaul_manche.get(),entry_poitrine.get(), entry_taille.get(), entry_long_taille.get(), entry_bassin.get(),\
        entry_lmanche.get(), entry_tmanche.get(),entry_pince.get(), entry_long_total.get(),entry_lrobe.get(),\
        entry_ceinture.get(),entry_cuisse.get(),entry_genoux.get(), entry_long_jupe.get(),entry_modele.get(),entry_retrait.get())
        if appartient(listes,pn):
            tkinter.messagebox.showerror(title='Formulaire invalide', message='Article déjà existant')
        else:
            listes.append(pn)
            tkinter.messagebox.showinfo(title='Validation réussie', message='Données enrégistrées '+'\n avec succès')
        
        insertion1='INSERT INTO Mesure(Dos,Epaul,Epaul_manche,Poitrine,Taille,Long_taille,Bassin,Tmanche,Lmanche,Pince,\
            Long_total,Lrobe,Ceinture,Cuisse,Genoux,Long_jupe,Modele,Dates)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        valeurs1=(entry_dos.get(),entry_epaul.get(),entry_epaul_manche.get(),entry_poitrine.get(),entry_taille.get(),entry_long_taille.get(),\
                entry_bassin.get(),entry_tmanche.get(),entry_lmanche.get(),entry_pince.get(),entry_long_total.get(),entry_lrobe.get(),\
                entry_ceinture.get(),entry_cuisse.get(),entry_genoux.get(),entry_long_jupe.get(),entry_modele.get(),Date)

        insertion2='INSERT INTO Clients(Nom,Prenom,Tel,Adresse)VALUES(%s,%s,%s,%s)'
        valeurs2=(entry_nom_client.get(),entry_prenom_client.get(),entry_tel_client.get(),entry_adresse.get())

        insertion3='INSERT INTO Personnel(Nom,Prenom,Tel)VALUES(%s,%s,%s)'
        valeurs3=(entry_nom_charge.get(),entry_prenom_charge.get(),entry_tel_charge.get())

        insertion4='INSERT INTO Payement(Prix,Avance,Reste,Date_retrait)VALUES(%s,%s,%s,%s)'
        valeurs4=(entry_prix.get(),entry_avance.get(),entry_reste.get(),entry_retrait.get())

        curseur.execute(insertion1,valeurs1),
        curseur.execute(insertion2,valeurs2),
        curseur.execute(insertion3,valeurs3),
        curseur.execute(insertion4,valeurs4)
        base.commit()
    else:
        tkinter.messagebox.showerror(title='Formulaire invalide', message='Toutes les champs doivent être renseignés')


def annuler():
    entry_nom_client.delete(0, END)
    entry_prenom_client.delete(0, END)
    entry_tel_client.delete(0, END)
    entry_adresse.delete(0, END)

    entry_nom_charge.delete(0, END)
    entry_prenom_charge.delete(0, END)
    entry_tel_charge.delete(0, END)

    entry_prix.delete(0, END)
    entry_avance.delete(0, END)
    entry_reste.delete(0, END)

def afficher():
    top=Toplevel(fen)
    top.geometry('1000x800+40+35')
    top.config(bg='gray25')
    #============================= Ecran =========================================================================================================================
    ecran=Text(top,font=('',11,'bold'),width=122,height=52,bd=7)
    ecran.pack()
    #============================= Insertion des données sur l'écran =============================================================================================
    ecran.insert(END,"\tMESURE\t\t CLIENT\t\t\t PERSONNEL\t\t PAYEMENT\t\t DATE")

    ecran.insert(END,'\n\nDos : %d'%(float(entry_dos.get()))),
    ecran.insert(END,'\t\t\tNom: %s'%(entry_nom_client.get())),
    ecran.insert(END,'\t\t\tNom: %s'%(entry_nom_charge.get())),
    ecran.insert(END,'\t\tPrix: %d'%(float(entry_prix.get()))),
    ecran.insert(END,'\t\t%s'%(Date))

    ecran.insert(END,'\n%s'%("-----------------------------------------------------------------------------------------------------------------------------------------------------------"))

    ecran.insert(END,'\n\nEpaul : %d'%(float(entry_epaul.get()))),
    ecran.insert(END,'\t\t\tPrenom: %s'%(entry_prenom_client.get())),
    ecran.insert(END,'\t\t\tPrenom: %s'%(entry_prenom_charge.get())),
    ecran.insert(END,'\t\tAvance: %d'%(float(entry_avance.get())))

    ecran.insert(END,'\n%s'%("-----------------------------------------------------------------------------------------------------------------------------------------------------------"))

    ecran.insert(END,'\n\nEpaul_manche : %d'%(float(entry_epaul_manche.get()))),
    ecran.insert(END,'\t\t\tTel: %s'%(entry_tel_client.get())),
    ecran.insert(END,'\t\t\tTel: %s'%(entry_tel_charge.get())),
    ecran.insert(END,'\t\tReste: %d'%(float(entry_reste.get())))

    ecran.insert(END,'\n%s'%("-----------------------------------------------------------------------------------------------------------------------------------------------------------"))

    ecran.insert(END,'\n\nPoitrine : %d'%(float(entry_poitrine.get()))),
    ecran.insert(END,'\t\t\tAdresse: %s'%(entry_adresse.get())),
    ecran.insert(END,'\t\t\t\t\tRetrait: %s'%(entry_retrait.get()))

    ecran.insert(END,'\n%s'%("-----------------------------------------------------------------------------------------------------------------------------------------------------------"))

    ecran.insert(END,'\n\nTaille : %d'%(float(entry_taille.get())))
    ecran.insert(END,'\n%s'%("-----------------------------------------------------------------------------------------------------------------------------------------------------------"))

    ecran.insert(END,'\n\nLong_taille : %d'%(float(entry_long_taille.get())))
    ecran.insert(END,'\n%s'%("-----------------------------------------------------------------------------------------------------------------------------------------------------------"))

    ecran.insert(END,'\n\nBassin : %d'%(float(entry_bassin.get())))
    ecran.insert(END,'\n%s'%("-----------------------------------------------------------------------------------------------------------------------------------------------------------"))

    ecran.insert(END,'\n\nLmanche : %d'%(float(entry_lmanche.get())))
    ecran.insert(END,'\n%s'%("-----------------------------------------------------------------------------------------------------------------------------------------------------------"))

    ecran.insert(END,'\n\nTmanche : %d'%(float(entry_tmanche.get())))
    ecran.insert(END,'\n%s'%("-----------------------------------------------------------------------------------------------------------------------------------------------------------"))

    ecran.insert(END,'\n\nPince : %d'%(float(entry_pince.get())))
    ecran.insert(END,'\n%s'%("-----------------------------------------------------------------------------------------------------------------------------------------------------------"))

    ecran.insert(END,'\n\nLong_total : %d'%(float(entry_long_total.get())))
    ecran.insert(END,'\n%s'%("-----------------------------------------------------------------------------------------------------------------------------------------------------------"))

    ecran.insert(END,'\n\nLrobe : %d'%(float(entry_lrobe.get())))
    ecran.insert(END,'\n%s'%("-----------------------------------------------------------------------------------------------------------------------------------------------------------"))

    ecran.insert(END,'\n\nCeinture : %d'%(float(entry_ceinture.get())))
    ecran.insert(END,'\n%s'%("-----------------------------------------------------------------------------------------------------------------------------------------------------------"))

    ecran.insert(END,'\n\nCuisse : %d'%(float(entry_cuisse.get())))
    ecran.insert(END,'\n%s'%("-----------------------------------------------------------------------------------------------------------------------------------------------------------"))

    ecran.insert(END,'\n\nGenoux : %d'%(float(entry_genoux.get())))
    ecran.insert(END,'\n%s'%("-----------------------------------------------------------------------------------------------------------------------------------------------------------"))

    ecran.insert(END,'\n\nLong_jupe : %d'%(float(entry_long_jupe.get())))
    ecran.insert(END,'\n%s'%("-----------------------------------------------------------------------------------------------------------------------------------------------------------"))

    ecran.insert(END,'\n\nModèle : %s'%(entry_modele.get()))
#================================= fonction pour le bouton vente ===================
maliste=[]
def vente():
    bat=Toplevel(fen)
    bat.geometry('1000x800+40+35')
    bat.config(bg='gray')

    titre=Label(bat,text='Articles',font=('',20,'bold'),bg='gray',fg='white')
    titre.place(x=30,y=20)
    article1=Entry(bat,font=('',9,'bold'),textvariable=StringVar(),width=30,bg='white')
    article1.place(x=8,y=80)
    article2=Entry(bat,font=('',9,'bold'),textvariable=StringVar(),width=30,bg='white')
    article2.place(x=8,y=160)
    article3=Entry(bat,font=('',9,'bold'),textvariable=StringVar(),width=30,bg='white')
    article3.place(x=8,y=240)
    article4=Entry(bat,font=('',9,'bold'),textvariable=StringVar(),width=30,bg='white')
    article4.place(x=8,y=320)
    article5=Entry(bat,font=('',9,'bold'),textvariable=StringVar(),width=30,bg='white')
    article5.place(x=8,y=400)
    article6=Entry(bat,font=('',9,'bold'),textvariable=StringVar(),width=30,bg='white')
    article6.place(x=8,y=480)
    article7=Entry(bat,font=('',9,'bold'),textvariable=StringVar(),width=30,bg='white')
    article7.place(x=8,y=560)
    article8=Entry(bat,font=('',9,'bold'),textvariable=StringVar(),width=30,bg='white')
    article8.place(x=8,y=640)
    article9=Entry(bat,font=('',9,'bold'),textvariable=StringVar(),width=30,bg='white')
    article9.place(x=8,y=720)

    titre=Label(bat,text='Quantité',font=('',20,'bold'),bg='gray',fg='white')
    titre.place(x=350,y=20)
    article11=Entry(bat,font=('',9,'bold'),width=10,bg='white',textvariable=DoubleVar())
    article11.place(x=350,y=80)
    article12=Entry(bat,font=('',9,'bold'),width=10,bg='white',textvariable=DoubleVar())
    article12.place(x=350,y=160)
    article13=Entry(bat,font=('',9,'bold'),width=10,bg='white',textvariable=DoubleVar())
    article13.place(x=350,y=240)
    article14=Entry(bat,font=('',9,'bold'),width=10,bg='white',textvariable=DoubleVar())
    article14.place(x=350,y=320)
    article15=Entry(bat,font=('',9,'bold'),width=10,bg='white',textvariable=DoubleVar())
    article15.place(x=350,y=400)
    article16=Entry(bat,font=('',9,'bold'),width=10,bg='white',textvariable=DoubleVar())
    article16.place(x=350,y=480)
    article17=Entry(bat,font=('',9,'bold'),width=10,bg='white',textvariable=DoubleVar())
    article17.place(x=350,y=560)
    article18=Entry(bat,font=('',9,'bold'),width=10,bg='white',textvariable=DoubleVar())
    article18.place(x=350,y=640)
    article19=Entry(bat,font=('',9,'bold'),width=10,bg='white',textvariable=DoubleVar())
    article19.place(x=350,y=720)

    titre=Label(bat,text='Prix',font=('',20,'bold'),bg='gray',fg='white')
    titre.place(x=550,y=20)
    article21=Entry(bat,font=('',9,'bold'),width=10,bg='white',textvariable=DoubleVar())
    article21.place(x=550,y=80)
    article22=Entry(bat,font=('',9,'bold'),width=10,bg='white',textvariable=DoubleVar())
    article22.place(x=550,y=160)
    article23=Entry(bat,font=('',9,'bold'),width=10,bg='white',textvariable=DoubleVar())
    article23.place(x=550,y=240)
    article24=Entry(bat,font=('',9,'bold'),width=10,bg='white',textvariable=DoubleVar())
    article24.place(x=550,y=320)
    article25=Entry(bat,font=('',9,'bold'),width=10,bg='white',textvariable=DoubleVar())
    article25.place(x=550,y=400)
    article26=Entry(bat,font=('',9,'bold'),width=10,bg='white',textvariable=DoubleVar())
    article26.place(x=550,y=480)
    article27=Entry(bat,font=('',9,'bold'),width=10,bg='white',textvariable=DoubleVar())
    article27.place(x=550,y=560)
    article28=Entry(bat,font=('',9,'bold'),width=10,bg='white',textvariable=DoubleVar())
    article28.place(x=550,y=640)
    article29=Entry(bat,font=('',9,'bold'),width=10,bg='white',textvariable=DoubleVar())
    article29.place(x=550,y=720)

    def total():
        somme=float(article11.get())*float(article21.get()) + float(article12.get())*float(article22.get()) + float(article13.get())*float(article23.get()) + \
            float(article14.get())*float(article24.get()) + float(article15.get())*float(article25.get()) + float(article16.get())*float(article26.get()) + \
            float(article17.get())*float(article27.get()) + float(article18.get())*float(article28.get()) + float(article19.get())*float(article29.get())
        total_entry.delete(0,END)
        total_entry.insert(0,somme)

    def afficher():
        #ecran_vente.delete(END)
        ecran_vente.insert(END,"Articles\t\tQuantité\t\tPrix")
        ecran_vente.insert(END,'\n\n%s'%(article1.get())),
        ecran_vente.insert(END,'\t\t%d'%float((article11.get()))),
        ecran_vente.insert(END,'\t\t%d'%float((article21.get())))

        ecran_vente.insert(END,'\n\n%s'%(article2.get())),
        ecran_vente.insert(END,'\t\t%d'%float((article12.get()))),
        ecran_vente.insert(END,'\t\t%d'%float((article22.get())))

        ecran_vente.insert(END,'\n\n%s'%(article3.get())),
        ecran_vente.insert(END,'\t\t%d'%float((article13.get()))),
        ecran_vente.insert(END,'\t\t%d'%float((article23.get())))

        ecran_vente.insert(END,'\n\n%s'%(article4.get())),
        ecran_vente.insert(END,'\t\t%d'%float((article14.get()))),
        ecran_vente.insert(END,'\t\t%d'%float((article24.get())))

        ecran_vente.insert(END,'\n\n%s'%(article5.get())),
        ecran_vente.insert(END,'\t\t%d'%float((article15.get()))),
        ecran_vente.insert(END,'\t\t%d'%float((article25.get())))

        ecran_vente.insert(END,'\n\n%s'%(article6.get())),
        ecran_vente.insert(END,'\t\t%d'%float((article16.get()))),
        ecran_vente.insert(END,'\t\t%d'%float((article26.get())))

        ecran_vente.insert(END,'\n\n%s'%(article7.get())),
        ecran_vente.insert(END,'\t\t%d'%float((article17.get()))),
        ecran_vente.insert(END,'\t\t%d'%float((article27.get())))

        ecran_vente.insert(END,'\n\n%s'%(article8.get())),
        ecran_vente.insert(END,'\t\t%d'%float((article18.get()))),
        ecran_vente.insert(END,'\t\t%d'%float((article28.get())))

        ecran_vente.insert(END,'\n\n%s'%(article9.get())),
        ecran_vente.insert(END,'\t\t%d'%float((article19.get()))),
        ecran_vente.insert(END,'\t\t%d'%float((article29.get())))

        ecran_vente.insert(END,"\n\n\nPrix total : "),
        ecran_vente.insert(END,'%d'%float(float(article11.get())*float(article21.get()) + float(article12.get())*float(article22.get()) + float(article13.get())*float(article23.get()) + \
            float(article14.get())*float(article24.get()) + float(article15.get())*float(article25.get()) + float(article16.get())*float(article26.get()) + \
            float(article17.get())*float(article27.get()) + float(article18.get())*float(article28.get()) + float(article19.get())*float(article29.get())))

    class Vente:
        def __init__(self,article1,article2,article3,article4,article5,article6,article7,article8,article9, \
                    article11,article12,article13,article14,article15,article16,article17,article18,article19, \
                    article21,article22,article23,article24,article25,article26,article27,article28,article29):
                    self.article1=article1,
                    self.article2=article2,
                    self.article3=article3,
                    self.article4=article4,
                    self.article5=article5,
                    self.article6=article6,
                    self.article7=article7,
                    self.article8=article8,
                    self.article9=article9,
                    self.article11=article11,
                    self.article12=article12,
                    self.article13=article13,
                    self.article14=article14,
                    self.article15=article15,
                    self.article16=article16,
                    self.article17=article17,
                    self.article18=article18,
                    self.article19=article19,
                    self.article21=article21,
                    self.article22=article22,
                    self.article23=article23,
                    self.article24=article24,
                    self.article25=article25,
                    self.article26=article26,
                    self.article27=article27,
                    self.article28=article28,
                    self.article29=article29

        def __eq__(self,other):
            return(self.article1==other.article1 and self.article2==other.article2 and self.article3==other.article3 and\
                self.article4==other.article4 and self.article5==other.article5 and self.article6==other.article6 and\
                self.article7==other.article7 and self.article8==other.article8 and self.article9==other.article9 and\
                self.article11==other.article11 and self.article12==other.article12 and self.article13==other.article13 and \
                self.article14==other.article14 and self.article15==other.article15 and self.article16==other.article16 and\
                self.article17==other.article17 and self.article18==other.article18 and self.article19==other.article19 and\
                self.article21==other.article21 and self.article22==other.article22 and self.article23==other.article23 and\
                self.article24==other.article24 and self.article25==other.article25 and self.article26==other.article26 and\
                self.article27==other.article27 and self.article28==other.article28 and self.article29==other.article29)          


    def Appartient(liste,val):
        for i in range(len(liste)):
            if liste[i].__eq__(val):
                return TRUE
        return FALSE    

    def valider():
        pt_unit1=float(article11.get())*float(article21.get())
        pt_unit2=float(article12.get())*float(article22.get())
        pt_unit3=float(article13.get())*float(article23.get())
        pt_unit4=float(article14.get())*float(article24.get())
        pt_unit5=float(article15.get())*float(article25.get())
        pt_unit6=float(article16.get())*float(article26.get())
        pt_unit7=float(article17.get())*float(article27.get())
        pt_unit8=float(article18.get())*float(article28.get())
        pt_unit9=float(article19.get())*float(article29.get())

        if article1.get()and article11.get()and article21.get():
            tkinter.messagebox.showinfo(title='Valider',message='Enrégistré')
            insertion='INSERT INTO Vente(Articles,Qt,Prix_unit,Pt_unit,Dates)VALUES(%s,%s,%s,%s,%s)'
            valeurs=((article1.get(),article11.get(),article21.get(),pt_unit1,Date))
            curseur.execute(insertion,valeurs)
            base.commit()

        elif article1.get()and article11.get()and article21.get() and article2.get()and article12.get()and article22.get():
             tkinter.messagebox.showinfo(title='Valider',message='Enrégistré')
             insertion='INSERT INTO Vente(Articles,Qt,Prix_unit,Pt_unit,Dates)VALUES(%s,%s,%s,%s,%s)'
             valeurs=((article1.get(),article11.get(),article21.get(),pt_unit1,Date),
             (article2.get(),article12.get(),article22.get(),pt_unit2,Date))
             curseur.executemany(insertion,valeurs)
             base.commit()

        elif article1.get()and article11.get()and article21.get() and article2.get()and article12.get()and article22.get() and\
             article3.get()and article13.get()and article23.get():
             tkinter.messagebox.showinfo(title='Valider',message='Enrégistré')

        elif article1.get()and article11.get()and article21.get() and article2.get()and article12.get()and article22.get() and\
             article3.get()and article13.get()and article23.get() and article4.get()and article14.get()and article24.get():
             tkinter.messagebox.showinfo(title='Valider',message='Enrégistré')

        elif article1.get()and article11.get()and article21.get() and article2.get()and article12.get()and article22.get() and\
             article3.get()and article13.get()and article23.get() and article4.get()and article14.get()and article24.get() and\
             article5.get()and article15.get() and article25.get():
             tkinter.messagebox.showinfo(title='Valider',message='Enrégistré')

        elif article1.get()and article11.get()and article21.get() and article2.get()and article12.get()and article22.get() and\
             article3.get()and article13.get()and article23.get() and article4.get()and article14.get()and article24.get() and\
             article5.get()and article15.get() and article25.get() and article6.get()and article16.get()and article26.get() :
             tkinter.messagebox.showinfo(title='Valider',message='Enrégistré')
        
        elif article1.get()and article11.get()and article21.get() and article2.get()and article12.get()and article22.get() and\
             article3.get()and article13.get()and article23.get() and article4.get()and article14.get()and article24.get() and\
             article5.get()and article15.get() and article25.get() and article6.get()and article16.get()and article26.get() and \
             article7.get()and article17.get()and article27.get():
             tkinter.messagebox.showinfo(title='Valider',message='Enrégistré')

        elif article1.get()and article11.get()and article21.get() and article2.get()and article12.get()and article22.get() and\
             article3.get()and article13.get()and article23.get() and article4.get()and article14.get()and article24.get() and\
             article5.get()and article15.get() and article25.get() and article6.get()and article16.get()and article26.get() and \
             article7.get()and article17.get()and article27.get() and article8.get()and article18.get()and article28.get():
             tkinter.messagebox.showinfo(title='Valider',message='Enrégistré')

        elif article1.get()and article11.get()and article21.get() and article2.get()and article12.get()and article22.get() and\
             article3.get()and article13.get()and article23.get() and article4.get()and article14.get()and article24.get() and\
             article5.get()and article15.get() and article25.get() and article6.get()and article16.get()and article26.get() and \
             article7.get()and article17.get()and article27.get() and article8.get()and article18.get()and article28.get():
             tkinter.messagebox.showinfo(title='Valider',message='Enrégistré')

        elif article1.get()and article11.get()and article21.get() and article2.get()and article12.get()and article22.get() and\
             article3.get()and article13.get()and article23.get() and article4.get()and article14.get()and article24.get() and\
             article5.get()and article15.get() and article25.get() and article6.get()and article16.get()and article26.get() and \
             article7.get()and article17.get()and article27.get() and article8.get()and article18.get()and article28.get():
             tkinter.messagebox.showinfo(title='Valider',message='Enrégistré')

        elif article1.get()and article2.get()and article3.get()and article4.get()and article5.get()and article6.get()and\
             article7.get()and article8.get()and article9.get()and article11.get()and article12.get()and article13.get()and\
             article14.get()and article15.get()and article16.get()and article17.get()and article18.get()and article19.get()and\
             article21.get()and article22.get()and article23.get()and article24.get()and article25.get()and article26.get()and\
             article27.get()and article28.get()and article29.get():
             tkinter.messagebox.showinfo(title='Valider',message='Enrégistré')
        else:
            tkinter.messagebox.showerror(title='Invalide',message='Champs vides')

            
            insertion='INSERT INTO Vente(Articles,Qt,Prix_unit,Pt_unit,Dates)VALUES(%s,%s,%s,%s,%s)'
            valeurs=((article1.get(),article11.get(),article21.get(),pt_unit1,Date),
                (article2.get(),article12.get(),article22.get(),pt_unit2,Date),
                (article3.get(),article13.get(),article23.get(),pt_unit3,Date),
                (article4.get(),article14.get(),article24.get(),pt_unit4,Date),
                (article5.get(),article15.get(),article25.get(),pt_unit5,Date),
                (article6.get(),article16.get(),article26.get(),pt_unit6,Date),
                (article7.get(),article17.get(),article27.get(),pt_unit7,Date),
                (article8.get(),article18.get(),article28.get(),pt_unit8,Date),
                (article9.get(),article19.get(),article29.get(),pt_unit9,Date))
            curseur.executemany(insertion,valeurs)
        """insertion='INSERT INTO Vente(Articles,Qt,Prix_unit,Pt_unit,Dates)VALUES(%s,%s,%s,%s,%s)'
        valeurs=((article1.get(),article11.get(),article21.get(),pt_unit1,Date))
        curseur.execute(insertion,valeurs)

        insertion='INSERT INTO Vente(Articles,Qt,Prix_unit,Pt_unit,Dates)VALUES(%s,%s,%s,%s,%s)'
        valeurs=((article2.get(),article12.get(),article22.get(),pt_unit2,Date))
        curseur.execute(insertion,valeurs)

        insertion='INSERT INTO Vente(Articles,Qt,Prix_unit,Pt_unit,Dates)VALUES(%s,%s,%s,%s,%s)'
        valeurs=((article3.get(),article13.get(),article23.get(),pt_unit3,Date))
        curseur.execute(insertion,valeurs)

        insertion='INSERT INTO Vente(Articles,Qt,Prix_unit,Pt_unit,Dates)VALUES(%s,%s,%s,%s,%s)'
        valeurs=((article4.get(),article14.get(),article24.get(),pt_unit4,Date))
        curseur.execute(insertion,valeurs)

        insertion='INSERT INTO Vente(Articles,Qt,Prix_unit,Pt_unit,Dates)VALUES(%s,%s,%s,%s,%s)'
        valeurs=((article5.get(),article15.get(),article25.get(),pt_unit5,Date))
        curseur.execute(insertion,valeurs)

        insertion='INSERT INTO Vente(Articles,Qt,Prix_unit,Pt_unit,Dates)VALUES(%s,%s,%s,%s,%s)'
        valeurs=((article6.get(),article16.get(),article26.get(),pt_unit6,Date))
        curseur.execute(insertion,valeurs)

        insertion='INSERT INTO Vente(Articles,Qt,Prix_unit,Pt_unit,Dates)VALUES(%s,%s,%s,%s,%s)'
        valeurs=((article7.get(),article17.get(),article27.get(),pt_unit7,Date))
        curseur.execute(insertion,valeurs)

        insertion='INSERT INTO Vente(Articles,Qt,Prix_unit,Pt_unit,Dates)VALUES(%s,%s,%s,%s,%s)'
        valeurs=((article8.get(),article18.get(),article22.get(),pt_unit8,Date))
        curseur.execute(insertion,valeurs)

        insertion='INSERT INTO Vente(Articles,Qt,Prix_unit,Pt_unit,Dates)VALUES(%s,%s,%s,%s,%s)'
        valeurs=((article9.get(),article19.get(),article29.get(),pt_unit9,Date))
        curseur.execute(insertion,valeurs)"""

        


    btn_valider=Button(bat,text='Valider',font=('',16,'bold'),width=13,bg='#E67E30',command=valider)
    btn_valider.place(x=750,y=750)
    btn_quit=Button(bat,text='Quitter',font=('',16,'bold'),width=13,bg='#E67E30',command=bat.destroy)
    btn_quit.place(x=450,y=750)
    btn_afficher=Button(bat,text='Afficher',font=('',16,'bold'),width=13,bg='#E67E30',command=afficher)
    btn_afficher.place(x=750,y=95)
    ecran_vente=Text(bat,width=40,height=30)
    ecran_vente.place(x=650,y=220)
    btn_total=Button(bat,text='Prix total',width=13,font=('',16,'bold'),bg='#E67E30',command=total)
    btn_total.place(x=750,y=145)    
    total_entry=Entry(bat,font=('',9,'bold'),width=30,bg='white',textvariable=DoubleVar())
    total_entry.place(x=728,y=185)


#=================================Labels============================================
lbl_vente=Label(fen,text='Pour effectuer une vente cliquer \nsur ce bouton merci !!!',font=('',16,'bold'),fg='white',bg='gray25')
lbl_vente.place(x=750,y=500)
lbl_titre=Label(canvas, text='MESURES',bg='#E67E30',font=('',14,'bold'))
lbl_titre.place(x=95,y=8)

lbl_dos=Label(canvas,text='Dos: ',bg='#E67E30',font=('',10,'bold'))
lbl_epaul=Label(canvas,text='Epaule: ',bg='#E67E30',font=('',10,'bold'))
lbl_epaul_manche=Label(canvas,text='Epaul Manche: ',bg='#E67E30',font=('',10,'bold'))
lbl_poitrine=Label(canvas,text='Poitrine: ',bg='#E67E30',font=('',10,'bold'))
lbl_taille=Label(canvas,text='Taille: ',bg='#E67E30',font=('',10,'bold'))
lbl_long_taille=Label(canvas,text='Long Taille: ',bg='#E67E30',font=('',10,'bold'))
lbl_bassin=Label(canvas,text='Bassin: ',bg='#E67E30',font=('',10,'bold'))
lbl_lmanche=Label(canvas,text='L.Manche: ',bg='#E67E30',font=('',10,'bold'))
lbl_tmanche=Label(canvas,text='T.Manche: ',bg='#E67E30',font=('',10,'bold'))
lbl_pince=Label(canvas,text='Pinces: ',bg='#E67E30',font=('',10,'bold'))
lbl_long_total=Label(canvas,text='Long Totale: ',bg='#E67E30',font=('',10,'bold'))
lbl_lrobe=Label(canvas,text='Long Robe: ',bg='#E67E30',font=('',10,'bold'))
lbl_ceinture=Label(canvas,text='Ceinture: ',bg='#E67E30',font=('',10,'bold'))
lbl_cuisse=Label(canvas,text='Cuisse: ',bg='#E67E30',font=('',10,'bold'))
lbl_genoux=Label(canvas,text='Genoux: ',bg='#E67E30',font=('',10,'bold'))
lbl_long_jupe=Label(canvas,text='Long Jupe: ',bg='#E67E30',font=('',10,'bold'))
lbl_modele=Label(canvas,text='Modèle: ',bg='#E67E30',font=('',12,'bold'),fg='white')

lbl_dos.place(x=10,y=60)
lbl_epaul.place(x=10,y=100)
lbl_epaul_manche.place(x=10,y=140)
lbl_poitrine.place(x=10,y=180)
lbl_taille.place(x=10,y=220)
lbl_long_taille.place(x=10,y=260)
lbl_bassin.place(x=10,y=300)
lbl_lmanche.place(x=10,y=340)
lbl_tmanche.place(x=10,y=380)
lbl_pince.place(x=10,y=420)
lbl_long_total.place(x=10,y=460)
lbl_lrobe.place(x=10,y=500)
lbl_ceinture.place(x=10,y=540)
lbl_cuisse.place(x=10,y=580)
lbl_genoux.place(x=10,y=620)
lbl_long_jupe.place(x=10,y=660)
lbl_modele.place(x=10,y=700)

#================================Entry=============================================
entry_dos=Entry(canvas,bg='white',font=('',9,'bold'),textvariable=entier1)
entry_epaul=Entry(canvas,bg='white',font=('',9,'bold'),textvariable=entier2)
entry_epaul_manche=Entry(canvas,bg='white',font=('',9,'bold'),textvariable=entier3)
entry_poitrine=Entry(canvas,bg='white',font=('',9,'bold'),textvariable=entier4)
entry_taille=Entry(canvas,bg='white',font=('',9,'bold'),textvariable=entier5)
entry_long_taille=Entry(canvas,bg='white',font=('',9,'bold'),textvariable=entier6)
entry_bassin=Entry(canvas,bg='white',font=('',9,'bold'),textvariable=entier7)
entry_lmanche=Entry(canvas,bg='white',font=('',9,'bold'),textvariable=entier8)
entry_tmanche=Entry(canvas,bg='white',font=('',9,'bold'),textvariable=entier9)
entry_pince=Entry(canvas,bg='white',font=('',9,'bold'),textvariable=entier10)
entry_long_total=Entry(canvas,bg='white',font=('',9,'bold'),textvariable=entier11)
entry_lrobe=Entry(canvas,bg='white',font=('',9,'bold'),textvariable=entier12)
entry_ceinture=Entry(canvas,bg='white',font=('',9,'bold'),textvariable=entier13)
entry_cuisse=Entry(canvas,bg='white',font=('',9,'bold'),textvariable=entier14)
entry_genoux=Entry(canvas,bg='white',font=('',9,'bold'),textvariable=entier15)
entry_long_jupe=Entry(canvas,bg='white',font=('',9,'bold'),textvariable=entier16)
entry_modele=Entry(canvas,bg='white',font=('',9,'bold'),textvariable=char1)

entry_dos.place(x=120,y=60)
entry_epaul.place(x=120,y=100)
entry_epaul_manche.place(x=120,y=140)
entry_poitrine.place(x=120,y=180)
entry_taille.place(x=120,y=220)
entry_long_taille.place(x=120,y=260)
entry_bassin.place(x=120,y=300)
entry_lmanche.place(x=120,y=340)
entry_tmanche.place(x=120,y=380)
entry_pince.place(x=120,y=420)
entry_long_total.place(x=120,y=460)
entry_lrobe.place(x=120,y=500)
entry_ceinture.place(x=120,y=540)
entry_cuisse.place(x=120,y=580)
entry_genoux.place(x=120,y=620)
entry_long_jupe.place(x=120,y=660)
entry_modele.place(x=120,y=700)

canvas.place(x= 10,y= 40)

#=================================Boite 2========================================
cvn=Canvas(fen,bg='white',width=300,height=350)
lbl_titre=Label(cvn, text='Info Client',bg='white',fg='#E67E30',font=('',14,'bold'))
lbl_titre.place(x=95,y=8)

lbl_nom_client=Label(cvn, text='Nom : ',font=('',9,'bold'),bg='white')
lbl_nom_client.place(x=10,y=60)
lbl_prenom_client=Label(cvn, text='Prenom : ',font=('',9,'bold'),bg='white')
lbl_prenom_client.place(x=10,y=100)
lbl_tel_client=Label(cvn, text='Tel : ',font=('',9,'bold'),bg='white')
lbl_tel_client.place(x=10,y=140)
lbl_adresse=Label(cvn, text='Adresse : ',font=('',9,'bold'),bg='white')
lbl_adresse.place(x=10,y=180)

cvn.place(x=340,y=80)

############################################### Entry ############################
entry_nom_client=Entry(cvn,textvariable=char2,font=('',9,'bold'))
entry_nom_client.place(x=120,y=60)
entry_prenom_client=Entry(cvn,textvariable=char3,font=('',9,'bold'))
entry_prenom_client.place(x=120,y=100)
entry_tel_client=Entry(cvn,textvariable=entier22,font=('',9,'bold'))
entry_tel_client.place(x=120,y=140)
entry_adresse=Entry(cvn,textvariable=char4,font=('',9,'bold'))
entry_adresse.place(x=120,y=180)

#=================================Boite 3========================================
cvn1=Canvas(fen,bg='seashell4',width=300,height=350)
lbl_titre=Label(cvn1, text='Personnel',bg='seashell4',font=('',14,'bold'))
lbl_titre.place(x=95,y=8)

lbl_nom_charge=Label(cvn1, text='Nom : ',font=('',9,'bold'),bg='seashell4')
lbl_nom_charge.place(x=10,y=60)
lbl_prenom_charge=Label(cvn1, text='Prenom : ',font=('',9,'bold'),bg='seashell4')
lbl_prenom_charge.place(x=10,y=100)
lbl_tel_charge=Label(cvn1, text='Tel : ',font=('',9,'bold'),bg='seashell4')
lbl_tel_charge.place(x=10,y=140)

############################################# Entry ###############################
entry_nom_charge=Entry(cvn1,textvariable=char5,font=('',9,'bold'))
entry_nom_charge.place(x=120,y=60)
entry_prenom_charge=Entry(cvn1,textvariable=char6,font=('',9,'bold'))
entry_prenom_charge.place(x=120,y=100)
entry_tel_charge=Entry(cvn1,textvariable=entier21,font=('',9,'bold'))
entry_tel_charge.place(x=120,y=140)

cvn1.place(x=340,y=440)

#=================================Boite 4======================================================================================================================
cvn2=Canvas(fen,bg='dark turquoise',width=300,height=240)
lbl_titre=Label(cvn2, text='Payement',bg='dark turquoise',font=('',14,'bold'))
lbl_titre.place(x=95,y=8)

lbl_prix=Label(cvn2,text='Prix : ',font=('',9,'bold'),bg='dark turquoise')
lbl_prix.place(x=10,y=60)
lbl_avance=Label(cvn2,text='Avance : ',font=('',9,'bold'),bg='dark turquoise')
lbl_avance.place(x=10,y=100)
lbl_reste=Label(cvn2,text='Reste : ',font=('',9,'bold'),bg='dark turquoise')
lbl_reste.place(x=10,y=140)
lbl_retrait=Label(cvn2,text='Date_retrait : ',font=('',9,'bold'),bg='dark turquoise')
lbl_retrait.place(x=10,y=180)

########################################## Entry ####################################
entry_prix=Entry(cvn2,textvariable=entier17,font=('',9,'bold'))
entry_prix.place(x=120,y=60)
entry_avance=Entry(cvn2,textvariable=entier18,font=('',9,'bold'))
entry_avance.place(x=120,y=100)
entry_reste=Entry(cvn2,textvariable=entier19,font=('',9,'bold'))
entry_reste.place(x=120,y=140)
entry_retrait=Entry(cvn2,textvariable=StringVar(),font=('',9,'bold'))
entry_retrait.place(x=120,y=180)

cvn2.place(x=670,y=40)

#============================== Boutons =======================================================================================================================
btn_valide=Button(fen,text='Valider',width=20,font=('',10,'bold'),bg='#E67E30',command=valider)
btn_valide.place(x=980,y=40)
btn_annuler=Button(fen,text='Annuler',width=20,font=('',10,'bold'),bg='#E67E30',command=annuler)
btn_annuler.place(x=980,y=180)
btn_quitter=Button(fen,text='Quitter',width=20,font=('',10,'bold'),bg='#E67E30',command=iExit)
btn_quitter.place(x=980,y=245)
btn_afficher=Button(fen,text='Afficher',width=20,font=('',10,'bold'),bg='#E67E30',command=afficher)
btn_afficher.place(x=980,y=110)
btn_vente=Button(fen,text='Vente',width=20,bd=8,height=4,font=('',16,'bold'),bg='#E67E30',command=vente)
btn_vente.place(x=780,y=600)

fen.mainloop()