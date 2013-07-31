"""
############################################################
Visual
############################################################

:Author: *Felipe Fagundes*

"""

import random

RAIO = 5
M_EXT = 25
M_INT = 10
SEP = 5
PEC_H = 10
PEC_V = 5
CASA = 40

ALTURA_ALVOS = 2*M_INT + 5*CASA + 2*SEP
ALTURA_INVENTARIO = 2*M_INT + (PEC_V*CASA) + (SEP*(PEC_V-1))

LARGURA = 800
ALTURA = 2*M_EXT + ALTURA_ALVOS + 2*CASA + ALTURA_INVENTARIO 

LETRAS = ["A", "B", "C"]


class Visual:
	"""Classe responsavel por desenhar o tabuleiro do jogo"""
	
	def __init__(self,doc,gui):
		"""Desenha o tabuleiro completo do jogo"""
		self.gui = gui
		self.canvas=gui.svg(width=LARGURA,height=ALTURA)
		doc["main"] <= self.canvas
		
	def build_base(self,gui):
		"""Desenha a base (fundo do tabuleiro)"""
		base=self.gui.rect(x=0, y= 0, width=LARGURA, height=ALTURA,rx = RAIO,fill="PaleTurquoise")
		self.canvas <= base
	
	def build_inventario(self,gui):
		"""Desenha o inventario no tabuleiro. O inventario e o local onde ficam as pecas no inicio do jogo"""
		x = M_EXT
		y = ALTURA_ALVOS + 2*CASA
		tabuleiro=self.gui.rect(x=x, y=y, width=PEC_H*(CASA+SEP)+2*M_INT, height=ALTURA_INVENTARIO,rx = RAIO,fill="DodgerBlue")
		self.canvas <= tabuleiro

		casas = [self.build_casa(self.canvas,
                                 x + M_INT + (CASA+SEP)*(c%PEC_H),
                                 y + M_INT + (CASA+SEP)*(c//PEC_H), "Gainsboro") for c in range(PEC_H * PEC_V)]
								 
								 
		return casas
		
	def build_casa(self,lugar,x,y, cor, tipo=None, id=None):
		"""Desenha uma casa no tabuleiro"""
		
		casa = self.gui.rect(x=0, y=0, width=CASA, height=CASA,rx=0,fill=cor)
		g = self.gui.g(transform = "translate(%d %d)"%(x,y), x=x, y=y)
		g <= casa
		lugar <= g
		return g	
		
    
	def build_alvos(self,gui):
		"""Desenha a base dos alvos. Ou seja, o lugar onde ficam as casas alvos e as casas com letras"""
		
		# Criando a base dos alvos
		x = M_EXT
		y = M_EXT
		alvos=self.gui.rect(x=x, y=y, width=13*(CASA+SEP)+2*M_INT, height=ALTURA_ALVOS,rx = RAIO,fill="DodgerBlue")
		self.canvas <= alvos

		# Criando as casas das letras
		letras = [self.build_casa(self.canvas,
                                 x + M_INT + (CASA+SEP)*(c%13),
                                 y + M_INT + (3*CASA+SEP)*(c//13), "Plum") for c in range(26)]
								 
		for casa in letras:
			build_letra(self,casa,LETRAS[random.randint(0,3)])
								 
		y = y + M_INT + CASA + SEP
								 
		# Criando as casas vazias
		casas = [self.build_casa(self.canvas,
                                 x + M_INT + (CASA+SEP)*(c%13),
                                 y + (3*CASA+SEP)*(c//13), "Gainsboro","alvo",c) for c in range(26)]
								 
								 
		return casas
		
	
	def build_peca(self, casa, id):
		""" """
								
		peca=self.gui.image(id="p" + str(id), x=casa.x, y=casa.y, width=40, height=40, href="/img/" + str(random.randint(1,9)) +".jpg", draggable=True)
		g = self.gui.g(id="gp" + str(id), transform="translate(-" + casa.x + ", -" + casa.y + ")")
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
		""" """					
		imagem=self.gui.image(id="p" + str(id), x=0, y=0, width=40, height=40, href="/img/letras/" + letra +".png", draggable=False)
		g = self.gui.g()
		g.ondragstart = self.no_drag
		g <= imagem
		casa <= g
		
	def no_drag(self, event):
		event.data.effectAllowed = "none"
								 
		
