#!/usr/bin/python



import webapp

class Redirector(webapp.webApp):
    """"Clase Redirectora"""


    redire = 1

    def parse(self , request):

        recurso = request.split(' ',2)[1]

        return request

    def process(self , peticion) :
        returnCode = '302 Found'
        htmlAnswer = '<html><body> La pagina se esta rediriguiendo a : >'  +
                    + str(redirector) + '<meta HTTP_EQUIV ="refresh" content = >' + str(redire) + '</>'


        return (returnCode , htmlAnswer)

    redire = redire +  0.5

if __name__=="__main__":
    testwebApp = Redirector ("localhost" , 1235)
