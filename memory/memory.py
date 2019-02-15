import numpy as np
import os

global Tableau_race_classe=np.zeros((0,0))


class skill():
	def __init__(self, name="", prerequis=[], fils=[]):
		self.name=str(self)
		self.pre=prerequis
		self.fils=fils
		self.desc=""
		self.name=name

	def __str__(self):
		sf=""
		if self.pre : sf+="liste des prerequis :\n"
		else : sf+="pas de prerequis\n"
		for i in self.pre: sf+="{}\n".format(i)
		sf+="\n Nom du skill : {}\n".format(self.name)
		if self.fils : sf+="Permet de debloquer : \n"
		else : sf+="ce skill ne permet pas d'en debloquer d'autres"
		for i in self.fils: sf+="{}\n".format(i)

	#La fonction ce dessous ajoute, mais n'enleve pas. On peut donc parfaitement imaginer que celui ci ajoute ligne a ligne depuis un fichier texte

	def add_desc(self, description): 
		self.desc+=description
		
