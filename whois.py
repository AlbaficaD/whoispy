#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Albafica de Fivezard 2016

#Fivezard.com By Daniel L (Albafica)

#Required libraries
import os
import sys
import argparse

#Function Whois
def whois(url):
	command = "whois "+url #Command used in terminal
	puente = os.popen(command)
	results = str(puente.read())
	return results 

#My Parser	
parser = argparse.ArgumentParser(description=" Whois site web")
parser.add_argument('-u', dest="op",help="url please",required=True)
arguments = parser.parse_args()

#In Case true
if (arguments.op):
 	target =arguments.op
	get = whois(target)
	name_file = target.rstrip(".com")
	name = name_file+".txt"
	archivo = open(name,'w')
	archivo.write(get)



	

