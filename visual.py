"""
############################################################
Visual
############################################################

:Author: *Carlo E. T. Oliveira*
:Author: *Kyle Kuo*
:Contact: carlo@nce.ufrj.br
:Date: 2013/04/09
:Status: This is a "work in progress"
:Revision: 0.1.1
:Home: `Labase <http://labase.selfip.org/>`__
:Copyright: 2013, `GPL <http://is.gd/3Udt>`__.
"""

import random

RAIO = 5
M_EXT = 25
M_INT = 10
SEP = 5
PEC_H = 8
PEC_V = 3
CASA = 40

ALTURA_ALVOS = 2*M_INT + 5*CASA + 2*SEP
ALTURA_INVENTARIO = 2*M_INT + (PEC_V*CASA) + (SEP*(PEC_V-1))

LARGURA = 800
ALTURA = 2*M_EXT + ALTURA_ALVOS + 2*CASA + ALTURA_INVENTARIO 

COLORS = ["red",
			"green",
			"blue",
			"#696969", #cinza
			"#EEB422", #amarelo 
			"#CD00CD"] #magenta


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
								 
		#pecas = [self.build_peca(casa) for casa in casas]
								 
		return casas
		
	def build_casa(self,lugar,x,y, cor, tipo=None, id=None):
		"""Desenha uma casa no tabuleiro"""
		
		casa = self.gui.rect(x=0, y=0, width=CASA, height=CASA,rx=0,fill=cor, id="rect")
		g = self.gui.g(transform = "translate(%d %d)"%(x,y))
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
								 
		y = y + M_INT + CASA + SEP
								 
		# Criando as casas vazias
		casas = [self.build_casa(self.canvas,
                                 x + M_INT + (CASA+SEP)*(c%13),
                                 y + (3*CASA+SEP)*(c//13), "Gainsboro","alvo",c) for c in range(26)]
								 
								 
		return casas
		
	
	def build_peca(self, casa, id):
		""" """
		peca=self.gui.ellipse(cx=CASA//2 , cy=CASA//2, ry=10,rx=10,fill=COLORS[random.randint(0,6)], id="p" + str(id), draggable=True)
		g = self.gui.g(draggable=True, id="gp" + str(id))
		g.onmouseover = self.muda_peca
		g.ondragstart = self.drag_start
		
		g <= peca
		casa <= g
		return g
		
	def muda_peca(self, event):
		#print('muda')
		#self.casa_visual.fill = "red"
		event.target.style.cursor = "pointer"
		
	def drag_start(self, ev):
		ev.data['id_peca']=ev.target.id
		print(ev.target.id)
		ev.data.effectAllowed = 'move'
    
		
	def build_mao(self, mao):
		""" """
		
		mao=self.gui.rect(x=0, y=0, width=CASA, height=CASA,rx = RAIO,fill="DodgerBlue")
		g = self.gui.g(transform = "translate(%d %d)"%(700,M_EXT))
		g <= mao
		self.canvas <= g
		return g
								 
		
