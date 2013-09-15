#! /usr/bin/env python
# -*- coding: UTF8 -*-
"""
############################################################
Chaves Logicas - Main
############################################################

:Author: *Carlo E. T. Oliveira*
:Author: *Felipe dos Santos Fagundes*
:Contact: fagundesfelipe2012@gmail.com
"""
from datetime import datetime
from bottle import route, view, run, get, post, static_file, request
import bottle
import os
import json
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
	

@get('/record')
def record_phase():
	try:
		doc_id, doc_rev = database.DRECORD.save({'nome': 'Archie', 'idade': '17'})
		json = get_json(request.params)
		record = database.DRECORD[doc_id]
        record["jogadas"] = json
        database.DRECORD[doc_id] = record
		return doc_id
	except Exception:
		return "Error in Database"
		pass
		

def get_json(request):
	data = {i: request[i] for i in request}
	print(data)
	return data
		

@get('/cadastrar_jogador')
def cadastrar_jogador():
	json = get_json(request.params)
	try:
		doc_id, doc_rev = database.DRECORD.save(json)
		return static_file("nivel1.html", root=DIR)
	except Exception:
		return "Error in Database"
		pass


if __name__ == "__main__":
	run(server='gunicorn', host='0.0.0.0', port=int(os.environ.get("PORT", 8080)), debug=True, workers=1)

app = bottle.default_app()