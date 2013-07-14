"""
############################################################
Chaves Logicas - Principal
############################################################
"""
from visual import Visual
from casa import Casa

class Jogo:
	def __init__(self, gui):
		"""Constroi as partes do Jogo. """
		self.build_base(gui)
		self.build_inventario(gui)
		self.build_alvos(gui)
		self.build_mao(gui)
		
	def build_base(self, gui):
		"""Gera a base do tabuleiro do jogo (O fundo do tabuleiro)"""
		self.base = gui.build_base(gui)
		
	def build_inventario(self, gui):
		""" """
		self.inventario = [Casa(casa_visual) for casa_visual in gui.build_inventario(gui)]
		
		pecas = [gui.build_peca(casa.casa_visual) for casa in self.inventario]
		
	def build_alvos(self, gui):
		""" """
		self.alvos = [Casa(casa_visual) for casa_visual in gui.build_alvos(gui)]
		
	def build_mao(self, gui):
		""" """
		self.mao = Casa(gui.build_mao(gui))
	
		
 
def main(doc,gui):
  print('Chaves Logicas')
  Jogo(Visual(doc,gui))
