# -*- coding: utf-8 -*-
import requests
# colors
BLACK = "\033[1;30m"
RED = "\033[1;31m"
GREEN = "\033[1;32m"
BLUE = "\033[1;94m"
YELLOW = "\033[1;33m"
CIANO = "\033[1;36m"
LIGHT_GREEN = "\033[1;92m"
WHITE = "\033[1;97m"
MAGENTA = "\033[1;35m"
LIGHT_RED = "\033[1;91m"
GREY = "\033[1;37m"
RESET = "\033[0;0m"
#end
 
host = input(LIGHT_GREEN + "Digite o IP Alvo Aqui ===>")
metodos = [CIANO + "GET", "POST", "OPTIONS", "PUT", "DELETE", "TRACE", "CONNECT", "HEAD", "PATCH"]
for metodo in metodos:
    resposta = requests.request(metodo, host)
    print (metodo + " |--> " + resposta.reason)

