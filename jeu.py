from tkinter import  *
import tkinter.messagebox
#import tkMessageBox
import os
import random
from helper import *
import time

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
		self.xC=None
		self.yC=None
		self.angle=None
		self.vitesse = 7
		self.nombreCoup = 0
		self.cible=[0,0]
		self.positionInitiale(x,y)
		
	def positionInitiale(self,x,y):
		self.xC = x
		self.yC = y
		if self.num == 0:
			self.x1=self.xC-15
			self.x2=self.xC+15
			self.y1=self.yC-35
			self.y2=self.yC+35
		elif self.num == 1:
			self.x1=self.xC-35
			self.x2=self.xC+35
			self.y1=self.yC-12
			self.y2=self.yC+12
		elif self.num == 2:
			self.x1=self.xC-15
			self.x2=self.xC+15
			self.y1=self.yC-25
			self.y2=self.yC+25
		elif self.num == 3:
			self.x1=self.xC-20
			self.x2=self.xC+20
			self.y1=y-20
			self.y2=y+20

	def bouge(self):
		if self.x1 <= 0 or self.x2 >= self.parent.largeur or self.y1 <= 0 or self.y2 >= self.parent.hauteur or self.parent.nombreCoup == 1:
			self.nombreCoup += random.randrange(4)
			if (self.nombreCoup%4) == 0:
				self.cible[0] =  (random.randrange(self.parent.largeur))
				self.cible[1] =  (self.parent.hauteur)
				print(self.cible)
				self.angle = Helper.calcAngle( (self.xC),  (self.yC),  (self.cible[0]),  (self.cible[1]))
			elif (self.nombreCoup%4) == 1:
				self.cible[0] =  (self.parent.largeur)
				self.cible[1] =  (random.randrange(self.parent.hauteur))
				self.angle = Helper.calcAngle( (self.xC),  (self.yC),  (self.cible[0]),  (self.cible[1]))
			elif (self.nombreCoup%4) == 2:
				self.cible[0] =  random.randrange(self.parent.largeur)
				self.cible[1] =  0
				self.angle = Helper.calcAngle( (self.xC),  (self.yC),  (self.cible[0]),  (self.cible[1]))
			elif (self.nombreCoup%4) == 3:
				self.cible[0] =  0
				self.cible[1] =  random.randrange(self.parent.hauteur)
				self.angle = Helper.calcAngle( (self.xC),  (self.yC),  (self.cible[0]),  (self.cible[1]))
			
		nouvX,nouvY = Helper.getAngledPoint(self.angle,self.vitesse,self.xC,self.yC)
		self.positionInitiale(nouvX, nouvY)
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
		self.nombreCoup = 0
		self.debutTime = 0
		self.finTime = 0
	
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

	def fermerTout(self):
		self.root.destroy()
		os._exit(1)
		
	def mortSubite(self):
		self.controleur.m.finTime = time.time()
		duree = self.controleur.m.finTime-self.controleur.m.debutTime
		tkinter.messagebox.showinfo("Oh non!", "Vous etes mort avec un temps de : "+str(format(duree, '.2f'))+" secondes.")
		#tkMessageBox.showinfo("Oh non!", "Vous etes mort...")
		self.fermerTout()
		
	def initPartie(self):
		self.canevas=Canvas(self.root,width=self.controleur.m.largeur,height=self.controleur.m.hauteur,bg="grey")
		self.canevas.pack()
		self.canevas.bind("<Button-1>",self.click)
		self.canevas.bind("<ButtonRelease>",self.relacherClick)
		self.canevas.bind("<Motion>",self.bouge)
		b = Button(self.root,text="Jouer Facile")
		b.pack(side=LEFT)	
		b = Button(self.root, text="Jouer Intermediaire")
		b.pack(side=LEFT)   
		b = Button(self.root, text="Jouer Difficile")
		b.pack(side=LEFT)   
		b = Button(self.root, text="Jouer Progressif")
		b.pack(side=LEFT)
		b = Button(self.root, text="High Scores")
		b.pack(side=LEFT)	   
		b = Button(self.root, text="Quitter", command=self.fermerTout)
		b.pack(side=LEFT) 
		
	def bouge(self,evt):
		if  self.carreBouge:
			self.controleur.carreBouge(evt.x,evt.y)
		
	def click(self,evt):
		lestags=self.canevas.gettags("current")
		if  "carre" in  lestags:
			self.carreBouge=1
			self.controleur.actif = 1
			if self.controleur.m.nombreCoup == 1:
				self.controleur.debutPartie()
				self.controleur.m.debutTime = time.time()
			
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