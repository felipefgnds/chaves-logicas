#! /usr/bin/env python
# -*- coding: UTF8 -*-
"""
############################################################
Chaves Logicas - Database
############################################################

:Author: *Carlo E. T. Oliveira*
:Author: *Felipe dos Santos Fagundes*
:Contact: fagundesfelipe2012@gmail.com

"""

from os import environ
from couchdb import Server

URL = environ.get('CLOUDANT_URL')
_DOCBASES = ['keystore']


class Activ(Server):
    "Active database"
    keystore = {}

    def __init__(self, url=URL):
        Server.__init__(self, url)
        act = self
        test_and_create = lambda doc: doc in act and act[doc] or act.create(doc)
        for attribute in _DOCBASES:
            setattr(Activ, attribute, test_and_create(attribute))

    def erase_database(self):
        'erase tables'
        for table in _DOCBASES:
            try:
                del self[table]
            except:
                pass


#try:
if True:
    __ACTIV = Activ()
    DRECORD = __ACTIV.keystore
#except Exception:
    #DRECORD = None


if __name__ == "__main__":
    #print([rec for rec in DRECORD])
    recs = {n: rec for n, rec in enumerate(DRECORD)}
    print (recs)
    ques = str(input("apaga?('apaga'/<indice>)"))
    if ques == 'apaga':
        __ACTIV.erase_database()
    elif int(ques) in recs:
        print (DRECORD[recs[int(ques)]])