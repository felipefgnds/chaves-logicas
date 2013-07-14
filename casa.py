"""
############################################################
Chaves Logicas - Classe Casa
############################################################
"""

class Casa:
	def __init__(self, casa_visual, mao,tipo):
		"""Constroi as partes do Jogo. """
		self.tipo=tipo
		self.casa_visual = casa_visual
		self.mao=mao
		self.peca=None
		self.casa_visual.onclick = self.manda_peca
		
	def manda_peca(self, event):
		if self.tipo == "comum":
			if self.peca is not None:
				if self.mao.peca is None:
					self.mao.pega_peca(self)
				else:
					self.troca_peca(self, self.mao)
			else:
				if self.mao.peca is not None:
					self.pega_peca(self.mao)
		else:
			print('clicou na mao')
		
	def pega_peca(self, casa):
		print('pega peca')
		self.casa_visual <= casa.peca
		self.peca = casa.peca
		casa.peca = None
		
	def troca_peca(self, casa1, casa2):
		aux = casa1.peca
		casa1.peca = None
		casa1.peca = casa2.peca
		casa1.casa_visual <= casa2.peca
		casa2.peca = None
		casa2.peca = aux
		casa2.casa_visual <= aux
	
		
	
		
	
		
	