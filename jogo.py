"""
###########################################################
Chaves Logicas - Jogo
###########################################################

:Author: *Felipe dos Santos Fagundes*

"""

# git push new master

from visual import Visual
from casa import Casa
import random

class Jogo:
	def __init__(self, doc, gui, nivel, id_jogador):
		"""Constroi as partes do Jogo."""
		self.build_base(gui)
		self.jogador=id_jogador
		
		req = ajax()
		req.on_complete = on_complete
		req.set_timeout(5,err_msg)
		req.open('GET','/get_pecas',True)
		req.send()
		
		if nivel==1 or nivel==5 :
			self.build_inventario(gui, doc)
			self.build_alvos(gui)
		
		if nivel==3 :
			self.build_deck(gui)
			self.build_grid(gui)
			
	
	def on_complete(req):
		if req.status==200 or req.status==0:
			doc["pecas"].value = req.text
		else:
			print("error "+req.text)
			
	def err_msg():
		print("Erro no Ajax")
		
		
	def build_base(self, gui):
		"""Gera a base do tabuleiro do jogo (O fundo do tabuleiro)"""
		self.base = gui.build_base(gui)
		
	def build_inventario(self, gui, doc):
		""" """
		# Criando as casas do inventario
		self.inventario = [Casa(casa_visual, None, "inventario", self.jogador, gui, doc) for casa_visual in gui.build_inventario(gui)]
		
		# Criando as pecas
		pecas = [gui.build_peca(casa.casa_visual, id) for id,casa in enumerate(self.inventario)]
		
		#pecas = []
		
		#for casa in self.inventario:
		#	peca = gui.build_peca(casa.casa_visual, gui.get_id_peca(random.randint(0,9), str(random.randint(1,4))))
		#	pecas.append(peca)
		
		map_pecas = {}
		
		
		# Alocando uma peca para cada casa do inventario
		for peca, casa in zip(pecas, self.inventario):
			map_pecas[peca.id] = casa
			casa.peca = peca
			casa.num_pecas_inicial = (PEC_H * PEC_V)
			
		self.map_pecas = map_pecas
		
		# Atrelando o mapeamento de pecas (informa a casa de uma determinada peca) nas casas do inventario
		for casa in self.inventario:
			casa.map_pecas=map_pecas
		
	def build_alvos(self, gui):
		""" """
		self.alvos = [Casa(casa_visual, self.map_pecas, "alvo", self.jogador) for casa_visual in gui.build_alvos(gui)]
		
	def build_grid(self, gui):
		""" """
		self.alvos = [Casa(casa_visual, self.map_pecas, "alvo", self.jogador) for casa_visual in gui.build_grid(gui)]
		
	def build_deck(self, gui):
		""" """
		# Criando as casas do inventario
		self.deck = [Casa(casa_visual, None, "inventario", self.jogador, gui) for casa_visual in gui.build_deck(gui)]
		
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
	
		
 
def main(doc,gui,nivel,id_jogador):
  print('Chaves Logicas')
  Jogo(doc,Visual(doc,gui,nivel),nivel,id_jogador)