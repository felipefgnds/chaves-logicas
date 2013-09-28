"""
###########################################################
Chaves Logicas - Clase Casa
###########################################################
"""
from visual import Visual
import svg

class Casa:
	def __init__(self, casa_visual, map_pecas,tipo=None, id_jogador=None, gui=None, doc=None):
		"""Constroi as partes do Jogo. """
		self.tipo=tipo
		self.casa_visual = casa_visual
		self.map_pecas = map_pecas
		self.peca=None
		self.num_pecas_inicial = None
		self.jogador = id_jogador
		self.gui=gui
		self.doc=doc
		
		
		self.casa_visual.ondragover = self.drag_over
		self.casa_visual.ondrop = self.drop
		self.casa_visual.onmouseover = self.mouse_over
			
	# quando se passa o mouse por cima da casa		
	def mouse_over(self, event):
		event.target.style.cursor = "auto"
	
	# quando se arrasta uma peca de uma casa
	def drag_over(self, event):
		event.data.dropEffect = 'move'
		event.preventDefault()
		event.target.style.cursor = "crosshair"
	
	# quando soltamos uma peca numa casa
	def drop(self, event):
		
		event.preventDefault()
		
		# resgatar a peca e sua casa de origem
		id_peca = event.data['id_peca']
		casa_atual = self.map_pecas['g' + id_peca]
		
		# verificar se a casa de destino esta vaga ou ocupada
		troca = False
		if self.peca is not None:
			if self.peca.id != casa_atual.peca.id :
				self.troca_peca(self, casa_atual)
				troca = True
				jogada = "troca"
		else:
			self.pega_peca(casa_atual)
			jogada = "encaixe"
		
		# montar requisicao para salvar dados da jogada
		req = ajax()
		req.on_complete = on_complete
		req.set_timeout(5,err_msg)
		
		if casa_atual.tipo=="alvo":
			origem = casa_atual.casa_visual.id
		else:
			origem = casa_atual.tipo
		
		if self.tipo=="alvo":
			destino = self.casa_visual.id
		else:
			destino = self.tipo
		
		req.open('GET','/salvar_jogada?id_jogador='+ self.jogador + '&origem=' + origem + '&destino=' + destino + '&peca=' + self.peca.img + '&tipo=' + jogada,False)
		req.send()
		
		if troca:
			req.open('GET','/salvar_jogada?id_jogador='+ self.jogador + '&origem=' + destino + '&destino=' + origem + '&peca=' + casa_atual.peca.img + '&tipo=' + jogada,True)
			req.send()
		
	def on_complete(req):
		if req.status==200 or req.status==0:
			print(req.text)
			return req.text
		else:
			print("error "+req.text)
			
	def err_msg():
		print("Erro no Ajax")
		
	# quando soltamos uma peca numa casa vazia	
	def pega_peca(self, casa):
		print('pega peca')
		
		altera_coordenadas(casa.peca,self.casa_visual.x,self.casa_visual.y)
		self.casa_visual <= casa.peca
		id_peca = casa.peca.id
		self.map_pecas[id_peca] = self
		
		self.peca = casa.peca
		casa.peca = None
		
		if casa.tipo == "inventario":
			id = int(casa.num_pecas_inicial) + int(casa.doc["pecas_extras_nv1"].value)
			nova_peca = casa.gui.build_peca(casa.casa_visual, str(id), self.peca.img.split("_")[0])
			casa.peca = nova_peca
			casa.map_pecas[nova_peca.id] = casa
			casa.doc["pecas_extras_nv1"].value = int(casa.doc["pecas_extras_nv1"].value) + 1
			
	# quando soltamos uma peca numa casa ocupada	
	def troca_peca(self, casa1, casa2):
		print("troca pecas")
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
	
	# ajusta as coordenadas de uma peca de acordo com sua nova casa 
	def altera_coordenadas(peca,x,y):
		peca.firstChild.firstChild.attributes.getNamedItem("x").nodeValue=x
		peca.firstChild.firstChild.attributes.getNamedItem("y").nodeValue=y
		peca.attributes.getNamedItem("transform").nodeValue = "translate(-" + x + ", -" + y + ")"
		
		
	
		
	
		
	
		
	