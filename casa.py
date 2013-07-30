"""
############################################################
Chaves Logicas - Classe Casa
############################################################
"""

class Casa:
	def __init__(self, casa_visual, map_pecas,tipo=None):
		"""Constroi as partes do Jogo. """
		self.tipo=tipo
		self.casa_visual = casa_visual
		self.map_pecas = map_pecas
		self.peca=None
		#self.casa_visual.onclick = self.manda_peca
		
		if tipo=="alvo" :
			self.casa_visual.ondragover = self.drag_over
			self.casa_visual.ondrop = self.drop
			self.casa_visual.onmouseover = self.mouse_over
			
			
	def mouse_over(self, event):
		event.target.style.cursor = "auto"
			
	def drag_over(self, event):
		event.data.dropEffect = 'move'
		event.preventDefault()
		event.target.style.cursor = "crosshair"
		
	def drop(self, event):
		print('drop')
		event.preventDefault()
		
		id_peca = event.data['id_peca']
		
		casa_atual = self.map_pecas['g' + id_peca]
		
		if self.peca is not None:
			if self.peca.id != casa_atual.peca.id :
				self.troca_peca(self, casa_atual)
		else:
			self.pega_peca(casa_atual)
		
		
	def pega_peca(self, casa):
		print('pega peca')
		self.casa_visual <= casa.peca
		id_peca = casa.peca.id
		self.map_pecas[id_peca] = self
		
		self.peca = casa.peca
		casa.peca = None
		
	def troca_peca(self, casa1, casa2):
		aux = casa1.peca
		casa1.peca = None
		casa1.peca = casa2.peca
		casa1.casa_visual <= casa2.peca
		self.map_pecas[casa2.peca.id] = casa1
		
		casa2.peca = None
		casa2.peca = aux
		casa2.casa_visual <= aux
		self.map_pecas[aux.id] = casa2
		
	
		
	
		
	
		
	