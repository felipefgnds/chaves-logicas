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
@view('./nivel1.html')
def cadastrar_jogador():
	json = get_json(request.params)
	try:
		doc_id, doc_rev = database.DRECORD.save(json)
		return dict(id_jogador=doc_id)
	except Exception:
		return "Erro no Banco de Dados"
		pass
		
@get('/salvar_jogada')
def salvar_jogada():
	try:
		record = database.DRECORD[request.params["id_jogador"]]
		jogadas = record["jogadas_nivel1"]
		if not isinstance(jogadas, list):
			jogadas = []
		jogadas.append({'timestamp': str(datetime.now()), 'origem': request.params["origem"], 'destino': request.params["destino"], 'peca': request.params["peca"], 'tipo': request.params["tipo"]})
		record["jogadas_nivel1"] = jogadas
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

@get('/analisar_nivel1')
@view('./nivel2.html')		
def analisar_nivel1():
	
	try:
		record = database.DRECORD[request.params["id_jogador"]]
		jogadas = record["jogadas_nivel1"]
		
		record["terminei_nivel1"] = request.params["terminei"]

		database.DRECORD[request.params["id_jogador"]] = record
		
		if not isinstance(jogadas, list):
			return "Não há jogadas cadastradas"
			
		pecas = database.DRECORD["_PECAS"]
		
		casas = {}
		
		for jogada in jogadas:
			if jogada["origem"] != "inventario":
				if jogada["tipo"] == "encaixe":
					casas[jogada["origem"]] = 0
			
			if jogada["destino"] != "inventario":
				casas[jogada["destino"]] = jogada["peca"]
				
		result = {"PRE":0, "SIL":0, "ALF":0}
		
		#string = ""
			
		
		for key in casas.keys():
			if casas[key] != 0:
				peca = pecas[str(casas[key])]
				if key in peca:
					result[peca[key]] += 1
				
		
		#for key in result.keys():
		#	string += key + " = " + str(result[key]) + "<br/>"
		
		#return string
		
		return dict(nome=record["nome"], id_jogador=request.params["id_jogador"])
		
	except Exception:
		return "Erro no Banco de Dados"
		pass

		
@post("/salvar_conte_me_nivel1")
def salvar_conte_me_nivel1():
	#try:
	record = database.DRECORD[request.params["id_jogador"]]
	conte_me = record["conte_me_nivel1"]
	record["conte_me_nivel1"] = request.params["conte_me_nivel1"]
	database.DRECORD[request.params["id_jogador"]] = record
		
	return "Ok."
	#except Exception:
	#	return "Erro no Banco de Dados"
	#	pass
	


if __name__ == "__main__":
	run(server='gunicorn', host='0.0.0.0', port=int(os.environ.get("PORT", 8080)), debug=True, workers=1)

app = bottle.default_app()