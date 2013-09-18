"""
############################################################
Chaves Logicas - Classe Casa
############################################################
"""

class Casa:
	def __init__(self, casa_visual, map_pecas,tipo=None, id_jogador=None):
		"""Constroi as partes do Jogo. """
		self.tipo=tipo
		self.casa_visual = casa_visual
		self.map_pecas = map_pecas
		self.peca=None
		self.jogador = id_jogador
		
		
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
		
		event.preventDefault()
		
		id_peca = event.data['id_peca']
		print('drop ' + id_peca)
		casa_atual = self.map_pecas['g' + id_peca]
		
		if self.peca is not None:
			if self.peca.id != casa_atual.peca.id :
				self.troca_peca(self, casa_atual)
		else:
			self.pega_peca(casa_atual)
		
		"""record = database.DRECORD[self.jogador]
		record["jogadas"] = {'origem': casa_atual.tipo, 'destino': self.tipo, 'peca': id_peca}
		database.DRECORD[self.jogador] = record"""
		
		req = ajax()
		req.on_complete = on_complete
		req.set_timeout(5,err_msg)
		req.open('GET','/salvar_jogada?id_jogador='+ self.jogador + '&origem=' + casa_atual.tipo + '&destino=' + self.tipo + '&peca=' + id_peca,True)
		req.send()
		
	def on_complete(req):
		print(req.readyState)
		print('status',req.status)
		if req.status==200 or req.status==0:
			print(req.text)
		else:
			print("error "+req.text)
			
	def err_msg():
		print("Erro no Ajax")
		
		
	def pega_peca(self, casa):
		print('pega peca')
		
		altera_coordenadas(casa.peca,self.casa_visual.x,self.casa_visual.y)
		self.casa_visual <= casa.peca
		id_peca = casa.peca.id
		self.map_pecas[id_peca] = self
		
		self.peca = casa.peca
		casa.peca = None
		
	def troca_peca(self, casa1, casa2):
		aux = casa1.peca
		casa1.peca = None
		casa1.peca = casa2.peca
		altera_coordenadas(casa2.peca, casa1.casa_visual.x, casa1.casa_visual.y)
		casa1.casa_visual <= casa2.peca
		self.map_pecas[casa2.peca.id] = casa1
		
		casa2.peca = None
		casa2.peca = aux
		altera_coordenadas(aux, casa2.casa_visual.x, casa2.casa_visual.y)
		casa2.casa_visual <= aux
		self.map_pecas[aux.id] = casa2
		
	def altera_coordenadas(peca,x,y):
		peca.firstChild.firstChild.attributes.getNamedItem("x").nodeValue=x
		peca.firstChild.firstChild.attributes.getNamedItem("y").nodeValue=y
		peca.attributes.getNamedItem("transform").nodeValue = "translate(-" + x + ", -" + y + ")"
		
		
	
		
	
		
	
		
	