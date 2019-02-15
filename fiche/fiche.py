import memory
from random import randint

class perso():
	def __init__(self, ad=0, ap=0, armor=50, MR=50, HP, Mana=0, Energy=0, agility, status=[],):
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

