from tkinter import *

class Carre():
	def __init__(self,parent):
		self.parent=parent 
		self.x1=280
		self.x2=320
		self.y1=280
		self.y2=320
		
	def bouge(self,x,y):
		self.x1=x-20
		self.x2=x+20
		self.y1=y-20
		self.y2=y+20

class Modele():
	def __init__(self, parent):
		self.controleur = parent
		self.carre=Carre(self)
	
	def carrebouge(self,x,y):
		self.carre.bouge(x,y)
		
class Controleur():
	def __init__(self):
		self.actif=1
		self.m = Modele(self)
		self.v = Vue(self)
		self.v.miseajour(self.m)
		self.debutPartie()
		self.v.root.mainloop()
		
	def carrebouge(self,x,y):
		self.m.carre.bouge(x,y)
		
	def debutPartie(self):
		if self.actif:
			self.v.miseajour(self.m)
			self.v.root.after(50,self.debutPartie)
		
class Vue():
	def __init__(self, parent):
		self.controleur = parent
		self.root = Tk()
		self.carrebouge=0
		self.root.wm_title("Carre Rouge")
		self.canevas=Canvas(self.root,width=450,height=450,bg="grey")
		self.canevas.pack()
		self.canevas.bind("<Button-1>",self.click)
		self.canevas.bind("<ButtonRelease>",self.relacherClick)
		self.canevas.bind("<Motion>",self.bouge)
		
	def bouge(self,evt):
		if self.carrebouge:
			self.controleur.carrebouge(evt.x,evt.y)
		
	def click(self,evt):
		lestags=self.canevas.gettags("current")
		if "carre" in lestags:
			self.carrebouge=1
			
	def relacherClick(self,evt):
		self.carrebouge=0
		
	def miseajour(self,modele):
		self.canevas.delete(ALL)
		j=modele.carre
		self.canevas.create_rectangle(j.x1,j.y1,j.x2,j.y2,fill="red", tags=("carre"))
		
if __name__ == '__main__':
	c=Controleur()