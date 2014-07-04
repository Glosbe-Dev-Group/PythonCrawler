import os
#========================================#
#os libreria para acceder a comandos de  #
#la terminal local                       #
#========================================#
try:
	print("\n\n\n\n\t\t:::::GlosbeDev::::\n\n\n\n")
	page = raw_input("ingresa una direccion url\n\n>:")
	#============================================#
	#raw_input() funciona para entrada de strings#
	#input() funciona para entrada de enteros    #
	#wget mas -r mas -p descarga una pagina web  #
	#============================================#
	os.system('wget  -r -p http://www.'+page)
except:
	print ("Error en algun parametro"+e)
