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
		self.cible = []
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
		'''
		if cible:
			pass
		else:
			x=random.randrange(self.parent.largeur)
			y=random.randrange(self.parent.hauteur)
			self.cible=[x,y]
		
		if self.num == 0:
			self.x1=x-10
			self.x2=x+10
			self.y1=y-10
			self.y2=y+10
		elif self.num == 1:
			self.x1=x-10
			self.x2=x+10
			self.y1=y-10
			self.y2=y+10
		elif self.num == 2:
			self.x1=x-10
			self.x2=x+10
			self.y1=y-10
			self.y2=y+10
		elif self.num == 3:
			self.x1=x-10
			self.x2=x+10
			self.y1=y-10
			self.y2=y+10
			'''
		pass

class   Modele():
	def __init__(self,  parent):
		self.controleur =   parent
		self.refreshRate = 10
		self.largeur = 1200
		self.hauteur = 450
		self.grandeurCarre = 30
		self.largeurBordure = 50
		self.pions = []
		self.carre=Carre(self)
		self.creerPions()
	
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
		
	def miseajour(self,modele):
		self.canevas.delete(ALL)
		j=modele.carre
		self.canevas.create_rectangle(0, 0, self.controleur.m.largeurBordure, self.controleur.m.hauteur, fill="black")
		self.canevas.create_rectangle(0, self.controleur.m.hauteur-self.controleur.m.largeurBordure, self.controleur.m.largeur, self.controleur.m.hauteur, fill="black")
		self.canevas.create_rectangle(0, 0, self.controleur.m.largeur, self.controleur.m.largeurBordure, fill="black")
		self.canevas.create_rectangle(self.controleur.m.largeur-self.controleur.m.largeurBordure, 0, self.controleur.m.largeur, self.controleur.m.hauteur, fill="black")
		for i in modele.pions:
			if self.controleur.actif == 1:
				i.bouge()
			self.canevas.create_rectangle(i.x1,i.y1,i.x2,i.y2,fill="blue", tags=("pion"))
		self.canevas.create_rectangle(j.x1,j.y1,j.x2,j.y2,fill="red",   tags=("carre"))
		self.canevas.addtag_overlapping("dessus",j.x1, j.y1, j.x2, j.y2)
		lestags=self.canevas.gettags("dessus")
		if "pion" in lestags:
			tkinter.messagebox.showinfo("Oh non!", "Vous etes mort...")
			#tkMessageBox.showinfo("Oh non!", "Vous etes mort...")
			self.root.destroy()
			os._exit(1)
		if  j.x1 <= self.controleur.m.largeurBordure:
			#j.x1 = self.controleur.m.largeurBordure
			#j.x2 = self.controleur.m.largeurBordure+self.controleur.m.grandeurCarre
			tkinter.messagebox.showinfo("Oh non!", "Vous etes mort...")
			#tkMessageBox.showinfo("Oh non!", "Vous etes mort...")
			self.root.destroy()
			os._exit(1)
		if  j.y1 <= self.controleur.m.largeurBordure:
			#j.y1 = self.controleur.m.largeurBordure
			#j.y2 = self.controleur.m.largeurBordure+self.controleur.m.grandeurCarre
			tkinter.messagebox.showinfo("Oh non!", "Vous etes mort...")
			#tkMessageBox.showinfo("Oh non!", "Vous etes mort...")
			self.root.destroy()
			os._exit(1)
		if  j.x2 > self.controleur.m.largeur - self.controleur.m.largeurBordure:
			#j.x1 = (self.controleur.m.largeur-self.controleur.m.largeurBordure) - self.controleur.m.grandeurCarre
			#j.x2 = self.controleur.m.largeur-self.controleur.m.largeurBordure
			tkinter.messagebox.showinfo("Oh non!", "Vous etes mort...")
			#tkMessageBox.showinfo("Oh non!", "Vous etes mort...")
			self.root.destroy()
			os._exit(1)
		if  j.y2 > self.controleur.m.hauteur - self.controleur.m.largeurBordure:
			#j.y1 = (self.controleur.m.hauteur-self.controleur.m.largeurBordure) - self.controleur.m.grandeurCarre
			#j.y2 = self.controleur.m.hauteur-self.controleur.m.largeurBordure
			tkinter.messagebox.showinfo("Oh non!", "Vous etes mort...")
			#tkMessageBox.showinfo("Oh non!", "Vous etes mort...")
			self.root.destroy()
			os._exit(1)
		
		
		
if  __name__    ==  '__main__':
	c=Controleur()