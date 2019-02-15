import memory
from Errorlist import *
from random import randint

class perso():
	def __init__(self, ad=0, ap=0, armor=50, MR=50, HP, Mana=0, Energy=0, agility, status=[]):
		self.ad=ad
		self.ap=ap
		self.armor=armor
		self.MR=MR
		self.HPmax=HP
		self.Mana=Mana
		self.En=Energy
		self.ag=agility
		self.sta=status


	def liststatus(self):
		return [memory.recognize(self.sta[i]) for i in self.sta]

	def create_temp_copy(self): #Note : penser à une façon efficace d'indentifier une copie de l'original, probablement en standardisant le nom des copies crées.
		return perso(ad=self.ad, ap=self.ap, armor=self.armor, MR=self.MR, self.HPmax, Mana=self.Mana, self.ag, status=self.sta)
		


###le but de cette class est de pouvoir travailler sur des feuilles sans modifier la feuille orignale, i.e. ne pas avoir a noter les max a l'interieur de la classe.###


class current_perso(perso): 
	def __init___(self, joueur): 			#joueur est de type perso()
		self.modele=perso.create_temp_copy(joueur)
		self.adcurrent=joueur.ad
                self.apcurrent=joueur.ap
                self.armorcurrent=joueur.armor
                self.MRcurrent=joueur.MR
                self.HPcurrent=joueur.HP
                self.Manacurrent=joueur.Mana
                self.Encurrent=joueur.En
                self.agcurrent=joueur.ag
                self.stacurrent=joueur.sta

	
	#on fait ensuite la liste des fonctions utiles a la gestion des buff/debuff temporaire, ainsi que des modificateurs sur les jauges qui seront amenées à évoluer

	#fonction un peu longuette dans le but de simplifier après: la longue liste d'elem par default permettra d'ecrire joueurcurr.modif_carac(Mana=-10), sans se soucier du nom de la fonction.

	def modif_carac(self, ad=0, ap=0, armor=0, MR=0, HP=0, Mana=0, Energy=0, agility=0):
		self.adcurrent+=ad
                self.apcurrent+=ap
                self.armorcurrent+=armor
                self.MRcurrent+=MR
                self.HPcurrent+=HP if self.HPcurrent+HP<0) else raise Deces
                self.Manacurrent+=Mana if self.Manacurrent+Mana<0) else raise NoMana
                self.Encurrent+=Energy if self.currentHP+HP<0) else raise NoEnergy
                self.agcurrent+=agility		

		
