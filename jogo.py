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

RANGE = {"NUM":[[1,81],[21,41]], 
         "ALF":[[41,61],[61,81]], 
		 "MIX":[[1,41],[41,81]]} 

class Jogo:

	def __init__(self, doc, gui, opcao, id_jogador, tela):
		"""Constroi as partes do Jogo."""
		
		self.range = RANGE[opcao][tela]
		self.opcao = opcao
		
		self.build_base(gui)
		self.jogador=id_jogador
		
		self.build_inventario(gui, doc)
		self.build_alvos(gui)
		
		
			
	
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
		self.inventario = [Casa(casa_visual, None, self, "inventario", gui) for casa_visual in gui.build_inventario(gui)]
		
				
		# Criando as pecas
		id_pecas = range(self.range[0],self.range[1])
		random.shuffle(id_pecas)
		
		
		pecas = [gui.build_peca(casa.casa_visual, id) for id,casa in zip(id_pecas, self.inventario)]
		
		#pecas = [gui.build_peca(casa.casa_visual, id) for id,casa in enumerate(self.inventario)]
		
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
		self.alvos = [Casa(casa_visual, self.map_pecas, self, "alvo") for casa_visual in gui.build_alvos(gui)]
	
		
 
def main(doc,gui,opcao,id_jogador, tela):
	print('Chaves Logicas')
	Jogo(doc,Visual(doc,gui,opcao, tela),opcao,id_jogador, tela)