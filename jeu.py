from    tkinter import  *
import tkinter.messagebox
import os

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

class   Modele():
	def __init__(self,  parent):
		self.controleur =   parent
		self.refreshRate = 10
		self.largeur = 450
		self.hauteur = 450
		self.grandeurCarre = 30
		self.largeurBordure = 50
		self.carre=Carre(self)
	
	def carrebouge(self,x,y):
		self.carre.bouge(x,y)
		
class   Controleur():
	def __init__(self):
		self.actif=1
		self.m  =   Modele(self)
		self.v  =   Vue(self)
		self.v.miseajour(self.m)
		self.debutPartie()
		self.v.root.mainloop()
		
	def carrebouge(self,x,y):
		self.m.carre.bouge(x,y)
		
	def debutPartie(self):
		if  self.actif:
			self.v.miseajour(self.m)
			self.v.root.after(self.m.refreshRate,self.debutPartie)
		
class   Vue():
	def __init__(self,  parent):
		self.controleur =   parent
		self.root   =   Tk()
		self.carrebouge=0
		self.root.wm_title("Carre   Rouge")
		self.canevas=Canvas(self.root,width=self.controleur.m.largeur,height=self.controleur.m.hauteur,bg="grey")
		self.canevas.pack()
		self.canevas.bind("<Button-1>",self.click)
		self.canevas.bind("<ButtonRelease>",self.relacherClick)
		self.canevas.bind("<Motion>",self.bouge)
		
		
	def bouge(self,evt):
		if  self.carrebouge:
			self.controleur.carrebouge(evt.x,evt.y)
		
	def click(self,evt):
		lestags=self.canevas.gettags("current")
		if  "carre" in  lestags:
			self.carrebouge=1
			
	def relacherClick(self,evt):
		self.carrebouge=0
		
	def miseajour(self,modele):
		self.canevas.delete(ALL)
		j=modele.carre
		if  j.x1 <= self.controleur.m.largeurBordure:
			#j.x1 = self.controleur.m.largeurBordure
			#j.x2 = self.controleur.m.largeurBordure+self.controleur.m.grandeurCarre
			tkinter.messagebox.showinfo("Oh non!", "Vous etes mort...")
			self.root.destroy()
			os._exit(1)
		if  j.y1 <= self.controleur.m.largeurBordure:
			#j.y1 = self.controleur.m.largeurBordure
			#j.y2 = self.controleur.m.largeurBordure+self.controleur.m.grandeurCarre
			tkinter.messagebox.showinfo("Oh non!", "Vous etes mort...")
			self.root.destroy()
			os._exit(1)
		if  j.x2 > self.controleur.m.largeur - self.controleur.m.largeurBordure:
			#j.x1 = (self.controleur.m.largeur-self.controleur.m.largeurBordure) - self.controleur.m.grandeurCarre
			#j.x2 = self.controleur.m.largeur-self.controleur.m.largeurBordure
			tkinter.messagebox.showinfo("Oh non!", "Vous etes mort...")
			self.root.destroy()
			os._exit(1)
		if  j.y2 > self.controleur.m.hauteur - self.controleur.m.largeurBordure:
			#j.y1 = (self.controleur.m.hauteur-self.controleur.m.largeurBordure) - self.controleur.m.grandeurCarre
			#j.y2 = self.controleur.m.hauteur-self.controleur.m.largeurBordure
			tkinter.messagebox.showinfo("Oh non!", "Vous etes mort...")
			self.root.destroy()
			os._exit(1)
			
		self.canevas.create_rectangle(0, 0, self.controleur.m.largeurBordure, self.controleur.m.hauteur, fill="black")
		self.canevas.create_rectangle(0, self.controleur.m.hauteur-self.controleur.m.largeurBordure, self.controleur.m.largeur, self.controleur.m.hauteur, fill="black")
		self.canevas.create_rectangle(0, 0, self.controleur.m.largeur, self.controleur.m.largeurBordure, fill="black")
		self.canevas.create_rectangle(self.controleur.m.largeur-self.controleur.m.largeurBordure, 0, self.controleur.m.largeur, self.controleur.m.hauteur, fill="black")
		self.canevas.create_rectangle(j.x1,j.y1,j.x2,j.y2,fill="red",   tags=("carre"))
		
		
if  __name__    ==  '__main__':
	c=Controleur()
