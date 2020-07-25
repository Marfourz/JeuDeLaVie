from tkinter import *
import time
from threading import Thread

class Etat(Thread):
    continuer=True
    def __init__(self,jeu):
        Thread.__init__(self)
        self.jeu = jeu
    def run(self):
        while Etat.continuer :
            self.jeu.commencer()
            time.sleep(0.5)

class JeuVie(Canvas):
    tableau=[]
    continuer=True
    def __init__(self,fenetre,width=800,height=800,**kargs):
        Canvas.__init__(self,fenetre,width=500,height=600,bg="white",**kargs)
        self.nbCase = 30
        self.longueur = height / self.nbCase
        self.largeur = width / self.nbCase
    def dessiner(self):
        for j in range(self.nbCase) :
            for i in range (self.nbCase):
                JeuVie.tableau.append(self.create_rectangle(self.largeur*i,self.longueur*j,self.largeur*(1+i),self.longueur*(1+j), outline="black",tags="white"))
    def determinerNumero(self,x,y):
        return int(int(y/self.longueur)*(self.nbCase)+int(x/self.largeur+1))
    
    def tuer(self,id):
        print("Debut")
        nbCasesViavants=0
        try:
            if self.gettags(id-self.nbCase-1)[0] == "black":
                        nbCasesViavants += 1
            if self.gettags(id-self.nbCase)[0] == "black":
                        nbCasesViavants += 1
            if self.gettags(id-self.nbCase+1)[0] == "black":
                        nbCasesViavants += 1
            if self.gettags(id-1)[0] == "black":
                        nbCasesViavants += 1
            if self.gettags(id+1)[0] == "black":
                        nbCasesViavants += 1
            if self.gettags(id+self.nbCase-1)[0] == "black":
                        nbCasesViavants += 1
            if self.gettags(id+self.nbCase)[0] == "black":
                        nbCasesViavants += 1
            if self.gettags(id+self.nbCase+1)[0] == "black":
                        nbCasesViavants += 1
            print(nbCasesViavants)
        except IndexError:
            pass
        if self.gettags(id)[0] == "black":
            if nbCasesViavants == 2 or nbCasesViavants == 3 :
                return False
            return True
        elif self.gettags(id)[0] == "white":
            if nbCasesViavants == 3 :
                return False
            return True

    def changerCouleur(self,event):
        if(self.gettags(self.determinerNumero(event.x,event.y))[0] == "white"):
            self.itemconfig(self.determinerNumero(event.x,event.y),fill="black",tag="black")
        else:
            self.itemconfig(self.determinerNumero(event.x,event.y),fill="black",tag="white")
        

    def commencer(self):
            morts = []
            vivants = []
            if JeuVie.continuer == True :
                for id in JeuVie.tableau : 
                    if (self.tuer(id)):
                        morts.append(id)
                    else :
                        vivants.append(id)
                for id in morts:
                    self.itemconfig(id,fill="white",tags="white")
                for id in vivants:
                    self.itemconfig(id,fill="black",tags="black")
    def stopper(self):
        for id in JeuVie.tableau :
            self.itemconfig(id,fill="white",tags="white")
            JeuVie.continuer = False
    


def pauses():
    JeuVie.continuer = False
    pause['text'] = "Continuer"
    pause['command'] = continuer

    
def continuer():
    JeuVie.continuer = True
    pause['text'] = "Pause"
    pause['command'] = pauses

def stopper():
    canvas.stopper()
    commence['text'] = "Commencer"
    commence['command'] = recommencer

def recommencer():
    JeuVie.continiuer = True
    commence['text'] = "Stopper"
    commence['command'] = stopper

def commencer() :
    etat.start()
    commence['text'] = "Stopper"
    pause.pack(side="left")
    commence['command'] = stopper

def quitter() :
    Etat.continuer = False
    fenetre.quit()

#Création des éléments
fenetre = Tk()
canvas=JeuVie(fenetre)
etat = Etat(canvas)
quitte=Button(fenetre,text="Quitter",command = quitter)
canvas.dessiner()
canvas.bind('<Button-1>',canvas.changerCouleur)

pause = Button(fenetre,text = "Pause",command = pauses)
titre=Label(fenetre,text="Jeu de la vie")
commence=Button(fenetre,text="Commencer",command = commencer)



#Poistionnement des éléments
titre.pack(side="top")
canvas.pack(side="top",fill=X)
commence.pack(side="left")
quitte.pack(side="right")
fenetre.mainloop()