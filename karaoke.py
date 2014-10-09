#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import os

import smallsmilhandler

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

import sys

if __name__ == "__main__":

	parser = make_parser()
	sHandler = smallsmilhandler.SmallSMILHandler()
	parser.setContentHandler(sHandler)
	parser.parse(open(sys.argv[1]))
	lista = sHandler.get_tags()

	for elemento in lista:
		tag = elemento[0]
		atribute = elemento[1]

		for value in atribute:
			if atribute[value] != '':
				if value == 'src':
					recurso = atribute[value]
					os.system("wget -q " + recurso)
					lista = recurso.split('/')
					lista = lista[-1]
					atribute[value] = lista
					print atribute[value]	 

