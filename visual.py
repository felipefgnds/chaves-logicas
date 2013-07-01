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
RAIO = 5
BASE = 600
ESPACO = 10

def main(doc):
  print('Quarto 0.1.0')

class Visual:
	"""Base do jogo com tabuleiro e duas maos."""
	def __init__(self,doc,gui):
		"""Constroi as partes do Jogo. """
		self.gui = gui
		self.canvas=gui.svg(width=BASE,height=BASE)
		doc["main"] <= self.canvas
		self.build_base()
		self.build_tabuleiro()
		self.build_alvos()
		
	def build_base(self,gui):
		"""docs here"""
		base=self.gui.rect(x=0, y= 0, width=BASE, height=BASE,rx = RAIO,fill="#8B7765")
		self.canvas <= base
	
	def build_tabuleiro(self,gui):
		"""docs here"""
		base=self.gui.rect(x=ESPACO, y=290, width=400, height=300,rx = RAIO,fill="NavajoWhite")
		self.canvas <= base
    
	def build_alvos(self,gui):
		"""docs here"""
		alvos=self.gui.rect(x=ESPACO, y=10, width=400, height=200,rx = RAIO,fill="NavajoWhite")
		self.canvas <= alvos
