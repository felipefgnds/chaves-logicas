#! /usr/bin/env python
# -*- coding: UTF8 -*-
"""
###########################################################
Chaves Logicas - Main
###########################################################

:Author: *Carlo E. T. Oliveira*
:Author: *Felipe dos Santos Fagundes*
:Contact: fagundesfelipe2012@gmail.com
"""
from bottle import route, view, run, get, post, static_file, request
from datetime import datetime
import bottle
import json
import os
import database

DIR = './'
		
@route('/hello')
def hello():
	return DIR


'''@get('/<filename:re:.*\.html>')
@get('/<filename:re:.*\.py>')
@get('/<filename:re:.*\.(jpg|png|gif|ico)>')
@get('/<filename:re:.*\.css>')
@get('/<filename:re:.*\.js>')'''
@get('/<filename:path>')
def file(filename):
	return static_file(filename, root=DIR)
		

def get_json(request):
	data = {i : request[i] for i in request}
	print(data)
	return data
		

@get('/cadastrar_jogador')
@view('./opcoes.html')
def cadastrar_jogador():
	json = get_json(request.params)
	try:
		doc_id = 0
		if "id_jogador" in request.params:
			doc_id = request.params["id_jogador"]
		else:
			doc_id, doc_rev = database.DRECORD.save(json)
		return dict(id_jogador=doc_id)
	except Exception:
		return "Erro no Banco de Dados"
		pass
		

@get('/tabuleiro')
@view('./tabuleiro.html')
def tabuleiro():
	return dict(id_jogador=request.params["id_jogador"], opcao=request.params["opcao"], tela=request.params["tela"])
	
@get('/opcoes')
@view('./opcoes.html')
def opcoes():
	return dict(id_jogador=request.params["id_jogador"])

@get('/conte_me')
@view('./conte_me.html')	
def conte_me():
	return dict(id_jogador=request.params["id_jogador"], opcao=request.params["opcao"], terminei=request.params["terminei"])

		
@get('/salvar_jogada')
def salvar_jogada():
	try:
		record = database.DRECORD[request.params["id_jogador"]]
		jogadas = record["jogadas_" + request.params["opcao"]]
		if not isinstance(jogadas, list):
			jogadas = []
		jogadas.append({'timestamp': str(datetime.now()), 'origem': request.params["origem"], 'destino': request.params["destino"], 'peca': request.params["peca"], 'tipo': request.params["tipo"]})
		record["jogadas_" + request.params["opcao"]] = jogadas
		database.DRECORD[request.params["id_jogador"]] = record
		return "Jogada salva no banco de dados"
	except Exception:
		return "Erro no Banco de Dados"
		pass
		
@get('/get_pecas')
def get_pecas():
	try:
		pecas = {}
		record = database.DRECORD["_PECAS"]
		
		ant = ""
		for peca in sorted(record.keys()):
			categoria = peca.split("_")[0]
			if len(categoria) > 0 :
				if categoria != ant :
					pecas[categoria] = []
				pecas[categoria].append(peca)
				ant = categoria
		
		string = ""
		for cat in pecas.keys():
			string += cat + "|"
			for peca in pecas[cat]:
				string += peca + ","
			string = string[:-1]
			string += ";"
		string = string[:-1]
			
		return string
	except Exception:
		return "Erro no Banco de Dados"
		pass

@get('/contar_pontuacao')
@view('./resultado.html')		
def contar_pontuacao():
	
		#try:
		record = database.DRECORD[request.params["id_jogador"]]
		jogadas = record["jogadas_" + request.params["opcao"]]
		
		record["conte_me_" + request.params["opcao"]] = request.params["conte_me"]
		record["terminei_" + request.params["opcao"]] = request.params["terminei"]

		database.DRECORD[request.params["id_jogador"]] = record
		
		if not isinstance(jogadas, list):
			return "Não há jogadas cadastradas"
			
		pecas = database.DRECORD["_CRIVO"]
		pecas = pecas["pecas"]
		
		casas = {}
		
		for jogada in jogadas:
			if jogada["origem"] != "inventario":
				if jogada["tipo"] == "encaixe":
					casas[jogada["origem"]] = 0
			
			if jogada["destino"] != "inventario":
				casas[jogada["destino"]] = jogada["peca"]
		
		#string = ""
			
		pontuacao_encaixe = 0
		pontuacao_pecas = 0
		
		for key in casas.keys():
			if casas[key] != 0:
				peca = pecas[str(casas[key])]
				pontuacao_pecas += int(peca["self"])
				if key in peca:
					pontuacao_encaixe += int(peca[key])
				
		
		string = "ENCAIXE = [" + str(pontuacao_encaixe) + "] <br/><br/> PECAS = [" + str(pontuacao_pecas) + "]"
		
		#return string
		
		return dict(nome=record["nome"], 
								id_jogador=request.params["id_jogador"],
								pontuacao_pecas=pontuacao_pecas,
								pontuacao_encaixe=pontuacao_encaixe)
		
		#except Exception:
		#return "Erro no Banco de Dados"
		#pass

		
@post("/salvar_conte_me")
@view('./resultado.html')
def salvar_conte_me():
	#try:
	record = database.DRECORD[request.params["id_jogador"]]
	
	record["conte_me_" + request.params["opcao"]] = request.params["conte_me"]
	record["terminei_" + request.params["opcao"]] = request.params["terminei"]
	
	database.DRECORD[request.params["id_jogador"]] = record
		
	return "Ok."
	#except Exception:
	#	return "Erro no Banco de Dados"
	#	pass
	

	
	
@get("/crivo")
def get_crivo():

	record = database.DRECORD["_CRIVO"]
	crivo = record["pecas"]
	
	string = "<table><tr><td>Peca</td><td>Pontuacao</td><td>Encaixe</td><td>Pontuacao</td></tr>"
	
	for peca in crivo.keys():
		for key in dict(crivo[peca]).keys():
			if key == "_":
				string += "<td>" + peca + "</td><td>" + str(crivo[peca][key]) + "</td>"
			else:
				string += "<td>" + key + "</td><td>" + str(crivo[peca][key]) + "</td>"
				
		string += "</tr>"
				
	string += "</table>"
	
	return string
	
	
@get("/crivo_json")
def get_crivo_json():

	pecas = range(1,71)
	
	string = "<table><tr>{</tr>"
	
	for peca in pecas:
		string += '<tr>"'+ str(peca) +'": {</tr> <tr>"_":x,</tr><tr>"BLX":<br/>x</tr> <tr>},</tr>'
				
	string += "}</table>"
	
	return string
	
	#return dict(crivo=string)
	
	
					
	
	

	
	


if __name__ == "__main__":
	run(server='gunicorn', host='0.0.0.0', port=int(os.environ.get("PORT", 8080)), debug=True, workers=1)

app = bottle.default_app()