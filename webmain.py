#! /usr/bin/env python
# -*- coding: UTF8 -*-
"""
############################################################
Pyndorama - Main
############################################################

:Author: *Carlo E. T. Oliveira*
:Contact: carlo@nce.ufrj.br
:Date: 2013/08/10
:Status: This is a "work in progress"
:Revision: 0.1.0
:Home: `Labase <http://labase.selfip.org/>`__
:Copyright: 2013, `GPL <http://is.gd/3Udt>`__.
"""
from datetime import datetime
from bottle import route, view, run, get, post, static_file, request
import bottle
import os
DIR = os.path.dirname(__file__)+'/'
ADM, HEA, PEC, PHA, END = 'adm1n head peca fase fim'.split()

#LIBS = DIR + '../libs/lib'
IMGS = DIR + '/'


@route('/')
def main():
        pass
		
@route('/hello')
def hello():
    return "Hello World!"


@get('/<name:re:.*\.html>')
def html(name):
    return static_file(name, root='/')


@get('/<filename:re:.*\.py>')
def python(filename):
    return static_file(filename, root=DIR)


@get('/<filename:re:.*\.(jpg|png|gif|ico)>')
def imagepng(filename):
    return static_file(filename, root=DIR)


@get('/<filename:re:.*\.css>')
def stylecss(filename):
    print(filename, IMGS)
    return static_file(filename, root=DIR)




if __name__ == "__main__":
    run(server='gunicorn', host='0.0.0.0', port=int(os.environ.get("PORT", 8080)), debug=True, workers=1)

app = bottle.default_app()