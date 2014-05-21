from tkinter import  *
import tkinter.messagebox
#import tkMessageBox
import os
import random

class   Carre():
	def __init__(self,parent):
		self.parent=parent  
		self.x1=(self.parent.largeur/2)-(self.parent.grandeurCarre/2)
		self.x2=(self.parent.largeur/2)+(self.parent.grandeurCarre/2)
		self.y1=(self.parent.hauteur/2)-(self.parent.grandeurCarre/2)
		self.y2=(self.parent.hauteur/2)+(self.parent.grandeurCarre/2)
		
	def bouge(self,x,y):
		self.x1=x-(self.parent.grandeurCarre/2)
		self.x2=x+(self.parent.grandeurCarre/2)
		self.y1=y-(self.parent.grandeurCarre/2)
		self.y2=y+(self.parent.grandeurCarre/2)

class Pion():
	def __init__(self,parent,x,y,nb):
		self.parent=parent 
		self.num=nb
		self.x1=None
		self.x2=None
		self.y1=None
		self.y2=None
		self.cible=None
		self.positionInitiale(x,y)
		
	def positionInitiale(self,x,y):
		if self.num == 0:
			self.x1=x-15
			self.x2=x+15
			self.y1=y-35
			self.y2=y+35
		elif self.num == 1:
			self.x1=x-35
			self.x2=x+35
			self.y1=y-12
			self.y2=y+12
		elif self.num == 2:
			self.x1=x-15
			self.x2=x+15
			self.y1=y-25
			self.y2=y+25
		elif self.num == 3:
			self.x1=x-20
			self.x2=x+20
			self.y1=y-20
			self.y2=y+20

	def bouge(self):
		blup = None
		if self.cible != None:
			if (self.x2-self.x1)/2 == self.cible[0] and (self.y2-self.y1)/2 == self.cible[1]:
				blup = True
			else:
				blup = False
		if blup == True or self.cible == None:
			if self.num == 0:
				if self.parent.nombreCoup%4 == 0:
					deplacementX = 1
					deplacementY = 1
					x=(self.parent.largeur - 15)*deplacementX
					y=random.randrange(self.parent.hauteur)*deplacementY
				elif self.parent.nombreCoup%4 == 1:
					deplacementX = 1
					deplacementY = -1
					x=100
					y=100
				elif self.parent.nombreCoup%4 == 2:
					deplacementX = -1
					deplacementY = -1
					x=100
					y=100
				elif self.parent.nombreCoup%4 == 3:
					deplacementX = -1
					deplacementY = 1
					x=100
					y=100
			elif self.num == 1:
				if self.parent.nombreCoup%4 == 0:
					deplacementX = -1
					deplacementY = 1
					x=100
					y=100
				elif self.parent.nombreCoup%4 == 1:
					deplacementX = -1
					deplacementY = -1
					x=100
					y=100
				elif self.parent.nombreCoup%4 == 2:
					deplacementX = 1
					deplacementY = -1
					x=100
					y=100
				elif self.parent.nombreCoup%4 == 3:
					deplacementX = 1
					deplacementY = 1
					x=100
					y=100
			elif self.num == 2:
				if self.parent.nombreCoup%4 == 0:
					deplacementX = -1
					deplacementY = -1
					x=100
					y=100
				elif self.parent.nombreCoup%4 == 1:
					deplacementX = -1
					deplacementY = 1
					x=100
					y=100
				elif self.parent.nombreCoup%4 == 2:
					deplacementX = 1
					deplacementY = 1
					x=100
					y=100
				elif self.parent.nombreCoup%4 == 3:
					deplacementX = 1
					deplacementY = -1
					x=100
					y=100
			elif self.num == 3:
				if self.parent.nombreCoup%4 == 0:
					deplacementX = 1
					deplacementY = -1
					x=100
					y=100
				elif self.parent.nombreCoup%4 == 1:
					deplacementX = 1
					deplacementY = 1
					x=100
					y=100
				elif self.parent.nombreCoup%4 == 2:
					deplacementX = -1
					deplacementY = 1
					x=100
					y=100
				elif self.parent.nombreCoup%4 == 3:
					deplacementX = -1
					deplacementY = -1
					x=100
					y=100
		
		if self.num == 0:
			self.x1=x-15
			self.x2=x+15
			self.y1=y-35
			self.y2=y+35
		elif self.num == 1:
			self.x1=x-35
			self.x2=x+35
			self.y1=y-12
			self.y2=y+12
		elif self.num == 2:
			self.x1=x-15
			self.x2=x+15
			self.y1=y-25
			self.y2=y+25
		elif self.num == 3:
			self.x1=x-20
			self.x2=x+20
			self.y1=y-20
			self.y2=y+20
		pass

class   Modele():
	def __init__(self,  parent):
		self.controleur =   parent
		self.refreshRate = 10
		self.largeur = 450
		self.hauteur = 450
		self.grandeurCarre = 30
		self.largeurBordure = 50
		self.pions = []
		self.carre=Carre(self)
		self.creerPions()
		self.vitesse = 1
		self.nombreCoup = 0
	
	def carreBouge(self,x,y):
		self.carre.bouge(x,y)

	def creerPions(self):
		for i in range(4):
			if i == 0:
				x = self.largeurBordure+40
				y = self.largeurBordure+40
			elif i == 1:
				x = self.largeur-(self.largeurBordure+40)
				y = self.largeurBordure+40
			elif i == 2:
				x = self.largeurBordure+40
				y = self.hauteur-(self.largeurBordure+40)
			elif i == 3:
				x = self.largeur-(self.largeurBordure+40)
				y = self.hauteur-(self.largeurBordure+40)
			self.pions.append(Pion(self,x,y,i))
		
	def miseajour(self):
		for i in self.pions:
			if self.controleur.actif == 1:
				i.bouge()
			self.controleur.v.dessinerPion(i)
		self.nombreCoup+=1	
			
	def gestionCollision(self,j):
		self.controleur.v.canevas.addtag_overlapping("dessus",j.x1, j.y1, j.x2, j.y2)
		lestags=self.controleur.v.canevas.gettags("dessus")
		if "pion" in lestags:
			self.controleur.v.mortSubite()
		if  j.x1 <= self.largeurBordure:
			self.controleur.v.mortSubite()
		if  j.y1 <= self.largeurBordure:
			self.controleur.v.mortSubite()
		if  j.x2 > self.largeur - self.largeurBordure:
			self.controleur.v.mortSubite()
		if  j.y2 > self.hauteur - self.largeurBordure:
			self.controleur.v.mortSubite()
			
class   Controleur():
	def __init__(self):
		self.actif=0
		self.m  =   Modele(self)
		self.v  =   Vue(self)
		self.v.miseajour(self.m)
		self.v.root.mainloop()
		
	def carreBouge(self,x,y):
		self.m.carre.bouge(x,y)
		
	def debutPartie(self):
		if  self.actif:
			self.v.miseajour(self.m)
			self.v.root.after(self.m.refreshRate,self.debutPartie)
		
class   Vue():
	def __init__(self,  parent):
		self.controleur =   parent
		self.root   =   Tk()
		self.carreBouge=0
		self.root.wm_title("Carre Rouge")
		self.initMenu()

	def initMenu(self):
		self.initPartie()

	def initHighScore(self):
		pass

	def initOptions(self):
		pass

	def fermerTout(self):
		self.root.destroy()
		os._exit(1)
		
	def mortSubite(self):
		tkinter.messagebox.showinfo("Oh non!", "Vous etes mort...")
		#tkMessageBox.showinfo("Oh non!", "Vous etes mort...")
		self.fermerTout()
		
	def initPartie(self):
		self.canevas=Canvas(self.root,width=self.controleur.m.largeur,height=self.controleur.m.hauteur,bg="grey")
		self.canevas.pack()
		self.canevas.bind("<Button-1>",self.click)
		self.canevas.bind("<ButtonRelease>",self.relacherClick)
		self.canevas.bind("<Motion>",self.bouge)
		
	def bouge(self,evt):
		if  self.carreBouge:
			self.controleur.carreBouge(evt.x,evt.y)
		
	def click(self,evt):
		lestags=self.canevas.gettags("current")
		if  "carre" in  lestags:
			self.carreBouge=1
			self.controleur.actif = 1
			self.controleur.debutPartie()
			
	def relacherClick(self,evt):
		self.carreBouge=0
		
	def dessinerPion(self,pionADessiner):
		self.canevas.create_rectangle(pionADessiner.x1,pionADessiner.y1,pionADessiner.x2,pionADessiner.y2,fill="blue", tags=("pion"))
		
	def miseajour(self,modele):
		self.canevas.delete(ALL)
		j=modele.carre
		self.canevas.create_rectangle(0, 0, self.controleur.m.largeurBordure, self.controleur.m.hauteur, fill="black")
		self.canevas.create_rectangle(0, self.controleur.m.hauteur-self.controleur.m.largeurBordure, self.controleur.m.largeur, self.controleur.m.hauteur, fill="black")
		self.canevas.create_rectangle(0, 0, self.controleur.m.largeur, self.controleur.m.largeurBordure, fill="black")
		self.canevas.create_rectangle(self.controleur.m.largeur-self.controleur.m.largeurBordure, 0, self.controleur.m.largeur, self.controleur.m.hauteur, fill="black")
		self.controleur.m.miseajour()
		self.canevas.create_rectangle(j.x1,j.y1,j.x2,j.y2,fill="red",   tags=("carre"))
		self.controleur.m.gestionCollision(j)
		
		
		
if  __name__    ==  '__main__':
	c=Controleur()