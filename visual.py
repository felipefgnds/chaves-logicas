"""
############################################################
Chaves Logicas - Classe Visual
############################################################

:Author: *Felipe dos Santos Fagundes*

"""

import random

RAIO = 5
M_EXT = 25
M_INT = 10
SEP = 5
PEC_H = 3
PEC_V = 3
CASA = 40

ALTURA_ALVOS = 2*M_INT + 5*CASA + 2*SEP
ALTURA_INVENTARIO = 2*M_INT + (PEC_V*CASA) + (SEP*(PEC_V-1))

CASAS_GRID_H = 16
CASAS_GRID_V = 10
ALTURA_GRID = 2*M_INT + CASAS_GRID_V*CASA

LARGURA = 800
ALTURA = 2*M_EXT + ALTURA_ALVOS + 2*CASA + ALTURA_INVENTARIO 

LETRAS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", 
			"K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
			
CAT_PECAS = ["NUM", "LTR", "PLV", "SLB", "IMG", "COR", "RBSC", "GRTJ", "TRC"]


class Visual:
	"""Classe responsavel por desenhar o tabuleiro do jogo"""
	
	def __init__(self,doc,gui,nivel):
		"""Desenha o tabuleiro completo do jogo"""
		self.gui = gui
		self.doc = doc
		self.canvas=gui.svg(width=LARGURA,height=ALTURA)
		doc["main"] <= self.canvas
		
		if nivel==1 or nivel==3:
			self.rx = 0
		else : 
			if nivel==5 :
				self.rx=20
	
		
	def get_id_peca(self, cat):
	
		# Carregando lista de pecas
		string = doc["pecas"].value
		string = string.split(";")
			
		pecas = {}
		for str in string:
			str = str.split("|")
			str_pecas = str[1].split(",")
			if str_pecas != "":
				pecas[str[0]] = str_pecas
			else:
				pecas[str[0]] = []
				
		if cat is None:
			cat = CAT_PECAS[random.randint(0,len(pecas))]
		
		if pecas[cat] == []:
			return None
			
		peca =  pecas[cat][random.randint(0,len(pecas[cat]))]
		pecas[cat].remove(peca)
		
		# Recriando a string com as pecas
		string = ""
		for categoria in pecas.keys():
			string += categoria + "|"
			
			if len(pecas[categoria]) > 0:
				for str_peca in pecas[categoria]:
					#print("PECA = [" + str_peca + "]")
					string += str_peca + ","
				string = string[:-1]
			string += ";"
		string = string[:-1]
		
		self.doc["pecas"].value = string
		
		return peca
				
			
		
		
	def build_base(self,gui):
		"""Desenha a base (fundo do tabuleiro)"""
		base=self.gui.rect(x=0, y= 0, width=LARGURA, height=ALTURA,rx=RAIO,fill="PaleTurquoise")
		self.canvas <= base
	
	def build_inventario(self,gui):
		"""Desenha o inventario no tabuleiro. O inventario e o local onde ficam as pecas no inicio do jogo"""
		x = M_EXT
		y = ALTURA_ALVOS + 2*CASA
		tabuleiro=self.gui.rect(x=x, y=y, width=PEC_H*(CASA+SEP)+2*M_INT, height=ALTURA_INVENTARIO,rx =self.rx,fill="DodgerBlue")
		self.canvas <= tabuleiro

		casas = [self.build_casa(self.canvas,
                                 x + M_INT + (CASA+SEP)*(c%PEC_H),
                                 y + M_INT + (CASA+SEP)*(c//PEC_H), "Gainsboro") for c in range(PEC_H * PEC_V)]
								 
								 
		return casas
		
	def build_deck(self,gui):
		"""Desenha o deck no tabuleiro. O deck e o local onde ficam as pecas no nivel 3"""
		x = M_EXT
		y = ALTURA_GRID + CASA
		deck=self.gui.rect(x=x, y=y, width=CASAS_GRID_H*(CASA+SEP)+2*M_INT, height=CASA+2*M_INT,rx = RAIO,fill="DodgerBlue")
		self.canvas <= deck

		casas = [self.build_casa(self.canvas,
									x + M_INT + (CASA+SEP)*(c%CASAS_GRID_H),
									y + M_INT + (CASA*SEP)*(c//CASAS_GRID_H), "Gainsboro") for c in range(CASAS_GRID_H)]
								 
								 
		return casas
		
	def build_casa(self,lugar,x,y, cor, tipo=None, id=None):
		"""Desenha uma casa no tabuleiro"""
		
		casa = self.gui.rect(x=0, y=0, width=CASA, height=CASA,rx=self.rx,fill=cor)
		
		if id is not None :
			id = "c" + LETRAS[id]
			g = self.gui.g(transform = "translate(%d %d)"%(x,y), x=x, y=y, id=id)
		else:
			g = self.gui.g(transform = "translate(%d %d)"%(x,y), x=x, y=y)
		g <= casa
		lugar <= g
		return g	
		 
	def build_alvos(self,gui):
		"""Desenha a base dos alvos. Ou seja, o lugar onde ficam as casas alvos e as casas com letras"""
		
		# Criando a base dos alvos
		x = M_EXT
		y = M_EXT
		alvos=self.gui.rect(x=x, y=y, width=13*(CASA+SEP)+2*M_INT, height=ALTURA_ALVOS,rx =self.rx,fill="DodgerBlue")
		self.canvas <= alvos

		# Criando as casas das letras
		letras = [self.build_casa(self.canvas,
                                 x + M_INT + (CASA+SEP)*(c%13),
                                 y + M_INT + (3*CASA+SEP)*(c//13), "Plum") for c in range(26)]
								 
		for casa,letra in zip(letras, LETRAS):
			build_letra(self,casa,letra)
								 
		y = y + M_INT + CASA + SEP
								 
		# Criando as casas vazias
		casas = [self.build_casa(self.canvas,
                                 x + M_INT + (CASA+SEP)*(c%13),
                                 y + (3*CASA+SEP)*(c//13), "Gainsboro","alvo",c) for c in range(26)]
								 
								 
		return casas
			
	def build_grid(self,gui):
		"""Desenha o grid onde ficam as casas alvos"""
		
		# Criando a base invisivel do grid
		x = M_EXT
		y = M_EXT
		alvos=self.gui.rect(x=x, y=y, width=CASAS_GRID_H*CASA+2*M_INT, height=ALTURA_GRID,rx = RAIO,fill="DodgerBlue")
		self.canvas <= alvos
								 
		y = M_EXT + M_INT;
								 
		# Criando as casas vazias
		casas = [self.build_casa(self.canvas,
                                 x + M_INT + (CASA)*(c%CASAS_GRID_H),
                                 y + (CASA)*(c//CASAS_GRID_H), "Gainsboro","alvo",c) for c in range(CASAS_GRID_V*CASAS_GRID_H)]
								 
								 
		return casas
		
	def build_peca(self, casa, id, cat=None):
		""" """
		img = self.get_id_peca(cat)
		
		
		
		if img is None:
			return None
		
		peca=self.gui.image(id="p" + str(id), x=casa.x, y=casa.y, width=40, height=40, href="/img/pecas/" + img +".JPG", draggable=True)
		g = self.gui.g(id="gp" + str(id), img=img, transform="translate(-" + casa.x + ", -" + casa.y + ")")
		g_auxiliar = self.gui.g()
		g_auxiliar.onmouseover = self.aponta_peca
		g_auxiliar.ondragstart = self.drag_start
		g_auxiliar <= peca
		g <= g_auxiliar
		casa <= g
		return g
		
	def aponta_peca(self, event):
		event.target.style.cursor = "pointer"
		
	def drag_start(self, event):
		event.data["id_peca"]=event.target.id
		print(event.target.id)
		event.data.effectAllowed = "move"
		
		
	def build_letra(self, casa, letra):
		""" Desenha as letras"""					
		imagem=self.gui.image(x=0, y=0, width=40, height=40, href="/img/letras/" + letra +".PNG", draggable=False)
		g = self.gui.g()
		g.ondragstart = self.no_drag
		g <= imagem
		casa <= g
		
	def no_drag(self, event):
		event.data.effectAllowed = "none"
								 
		
