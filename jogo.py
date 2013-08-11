"""
############################################################
Chaves Logicas - Principal
############################################################
"""

# git push new master

from visual import Visual
from casa import Casa

class Jogo:
	def __init__(self, gui, nivel):
		"""Constroi as partes do Jogo. """
		self.build_base(gui)
		
		if nivel==1 :
			self.build_inventario(gui)
			self.build_alvos(gui)
		
		if nivel==3 :
			self.build_deck(gui)
			self.build_grid(gui)
		
		
	def build_base(self, gui):
		"""Gera a base do tabuleiro do jogo (O fundo do tabuleiro)"""
		self.base = gui.build_base(gui)
		
	def build_inventario(self, gui):
		""" """
		# Criando as casas do inventario
		self.inventario = [Casa(casa_visual, None, "alvo") for casa_visual in gui.build_inventario(gui)]
		
		# Criando as pecas
		pecas = [gui.build_peca(casa.casa_visual, id) for id,casa in enumerate(self.inventario)]
		
		map_pecas = {}
		
		# Alocando uma peca para cada casa do inventario
		for peca, casa in zip(pecas, self.inventario):
			map_pecas[peca.id] = casa
			casa.peca=peca
			
		self.map_pecas = map_pecas
		
		# Atrelando o mapeamento de pecas (informa a casa de uma determinada peca) nas casas do inventario
		for casa in self.inventario:
			casa.map_pecas=map_pecas
		
	def build_alvos(self, gui):
		""" """
		self.alvos = [Casa(casa_visual, self.map_pecas, "alvo") for casa_visual in gui.build_alvos(gui)]
		
	def build_grid(self, gui):
		""" """
		self.alvos = [Casa(casa_visual, self.map_pecas, "alvo") for casa_visual in gui.build_grid(gui)]
		
	def build_deck(self, gui):
		""" """
		# Criando as casas do inventario
		self.deck = [Casa(casa_visual, None, "alvo") for casa_visual in gui.build_deck(gui)]
		
		# Criando as pecas
		pecas = [gui.build_peca(casa.casa_visual, id) for id,casa in enumerate(self.deck)]
		
		map_pecas = {}
		
		# Alocando uma peca para cada casa do inventario
		for peca, casa in zip(pecas, self.deck):
			map_pecas[peca.id] = casa
			casa.peca=peca
			
		self.map_pecas = map_pecas
		
		# Atrelando o mapeamento de pecas (informa a casa de uma determinada peca) nas casas do inventario
		for casa in self.deck:
			casa.map_pecas=map_pecas
	
		
 
def main(doc,gui,nivel):
  print('Chaves Logicas')
  Jogo(Visual(doc,gui),nivel)

