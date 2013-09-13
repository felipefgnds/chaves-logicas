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
	

@post('/record')
def record_phase():
	try:
		doc_id, doc_rev = database.DRECORD.save({'nome': 'Archie', 'idade': '17'})
		print(doc_id)
	except Exception:
		return "Error in Database"
		pass
   """ try:
        json = retrieve_data(request.params)
        record_id = json.keys()[0]
        record = database.DRECORD[record_id]
        record[PHA] += [json[record_id]]
        database.DRECORD[record_id] = record
        return record
    except Exception:
        return "Fase dd jogo não foi gravado %s" % str(request.params.values())"""



if __name__ == "__main__":
	run(server='gunicorn', host='0.0.0.0', port=int(os.environ.get("PORT", 8080)), debug=True, workers=1)

app = bottle.default_app()