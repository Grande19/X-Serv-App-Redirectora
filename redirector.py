#!usr/bin/python
#-*- coding: utf-8 -

import webApp
import socket

class Redirector(webApp.webApp):
    """"Clase Redirectora"""


    redirector = 1

    def parse(self , request):

        recurso = request.split(' ',2)[1]

        return request

    def process(self , peticion) :
        returnCode = '302 Found'
        htmlAnswer = '<html><body> La pagina' + str(recurso) + 'se está rediriguiendo a :' +
                    str(redirector) + <'meta HTTP_EQUIV ="refresh" content = ' + str(redirector) + '/'>


    return (returnCode , htmlAnswer)

    redirector = redirector +  0.5

if __name__=="__main__":
    testWebApp = Redirector ("localhost" , 1235)
