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
PEC_H = 1
PEC_V = 1
CASA = 78

ALTURA_ALVOS = 4*M_INT + 2*CASA + 2*SEP

#LARGURA_INVENTARIO = PEC_H*(CASA+SEP)+2*M_INT

LARGURA = 920
ALTURA = 2*M_EXT + ALTURA_ALVOS + 2*CASA 

NUM_PECAS = {"NUM":[10,4], "ALF":[10,4], "MIX":[10,8]} 

class Visual:
	"""Classe responsavel por desenhar o tabuleiro do jogo"""
	
	def __init__(self,doc,gui,opcao):
		"""Desenha o tabuleiro completo do jogo"""
		self.gui = gui
		self.doc = doc
		
		self.pec_h = NUM_PECAS[opcao][0]
		self.pec_v = NUM_PECAS[opcao][1]
		
		self.canvas_alvos=gui.svg(width=LARGURA,height=ALTURA_ALVOS)
		doc["alvos"] <= self.canvas_alvos
		
		self.canvas=gui.svg(width=LARGURA,height=ALTURA + 2*M_INT + (self.pec_v*CASA) + (SEP*(self.pec_v-1)))
		doc["inventario"] <= self.canvas
		
		self.rx=0
		
		
	def build_base(self,gui):
		"""Desenha a base (fundo do tabuleiro)"""
		base=self.gui.rect(x=0, y= 0, width=LARGURA, height=ALTURA + 2*M_INT + (self.pec_v*CASA) + (SEP*(self.pec_v-1)),rx=RAIO,fill="PaleTurquoise")
		self.canvas <= base
	
	def build_inventario(self,gui):
		"""Desenha o inventario no tabuleiro. O inventario e o local onde ficam as pecas no inicio do jogo"""
		x = M_EXT
		y = ALTURA_ALVOS + CASA
		tabuleiro=self.gui.rect(x=x, y=y, width=self.pec_h*(CASA+SEP)+2*M_INT, height=2*M_INT + (self.pec_v*CASA) + (SEP*(self.pec_v-1)),rx =self.rx,fill="DodgerBlue")
		self.canvas <= tabuleiro

		casas = [self.build_casa(self.canvas,
                                 x + M_INT + (CASA+SEP)*(c%self.pec_h),
                                 y + M_INT + (CASA+SEP)*(c//self.pec_h), "Gainsboro") for c in range(self.pec_h * self.pec_v)]
								 
								 
		return casas
		
	def build_casa(self,lugar,x,y, cor, tipo=None, id=None):
		"""Desenha uma casa no tabuleiro"""
		
		casa = self.gui.rect(x=0, y=0, width=CASA, height=CASA,rx=self.rx,fill=cor)
		
		if id is not None :
			id = "c" + str(id)
			g = self.gui.g(transform = "translate(%d %d)"%(x,y), x=x, y=y, id=id)
		else:
			g = self.gui.g(transform = "translate(%d %d)"%(x,y), x=x, y=y)
		g <= casa
		lugar <= g
		return g	
		 
	def build_alvos(self,gui):
		"""Desenha a base dos alvos. Ou seja, o lugar onde ficam as casas alvos e as casas com letras"""
		
		# Criando a base dos alvos
		#x = M_EXT
		#y = M_EXT
		x=0
		y=0
		"""10*(CASA+SEP)+2*M_INT"""
		alvos=self.gui.rect(x=x, y=y, width=LARGURA, height=ALTURA_ALVOS,rx =self.rx,fill="Black")
		self.canvas_alvos <= alvos
		
		x = M_EXT
		y = M_EXT

		# Criando as casas das imagens
		imagens = [self.build_casa(self.canvas_alvos,
                                 x + M_INT + (CASA+SEP)*(c%10),
                                 y + M_INT + (3*CASA+SEP)*(c//10), "Plum") for c in range(10)]
								 
		for num,casa in enumerate(imagens):
			build_imagem(self,casa,num+1)
								 
		y = y + M_INT + CASA + SEP
								 
		# Criando as casas vazias (encaixes)
		casas = [self.build_casa(self.canvas_alvos,
                                 x + M_INT + (CASA+SEP)*(c%10),
                                 y + (3*CASA+SEP)*(c//10), "Gainsboro","alvo",c) for c in range(10)]
								 
								 
		return casas
			
		
	def build_peca(self, casa, img):
		""" """
		#img = self.get_id_peca(cat)
		
		#if img is None:
		#	return None
		
		id = int(doc["id_casa"].value) + 1
		doc["id_casa"].value = id
		
		
		peca=self.gui.image(id="p" + str(id), x=casa.x, y=casa.y, width=CASA, height=CASA, href="/img/pecas/" + str(img) +".PNG", draggable=True)
		g = self.gui.g(id="gp" + str(id), img=str(img), transform="translate(-" + casa.x + ", -" + casa.y + ")")
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
		
		
	def build_imagem(self, casa, num):
		""" Desenha as letras"""					
		imagem=self.gui.image(x=0, y=0, width=CASA, height=CASA, href="/img/alvos_numericos/" + str(num) +".PNG", draggable=False)
		g = self.gui.g()
		g.ondragstart = self.no_drag
		g <= imagem
		casa <= g
		
	def no_drag(self, event):
		event.data.effectAllowed = "none"
								 
		
