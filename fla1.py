import requests
import os
#import Dweet
import time

dweetEnvia = "https://dweet.io/dweet/for/"
nome = "fla"
var1 = "Temperatura"
var2 = "led"
var3 = "SistemaDesligado"
dweetRecebe = "http://dweet.io:443/get/lastest/dweet/for/fla"
valor = 1
val1 = 0

#dweet root domain and endpoints
BASE_URL = "http://dweet.io:443/"

#creates a name for the thing dweeting.
#for anonymous or first time use.
#assigns a random dweet name to the thing.
DWEET = "{0}{1}".format(BASE_URL , "dweet?")
#dweet by thing name.
DWEET_BY_NAME = "{0}{1}".format(BASE_URL, "dweet/for/{name}?")

#get latest dweets by name.
LATEST_DWEET = "{0}{1}".format(BASE_URL, "get/latest/dweet/for/{name}")

#get all dweets by name.
ALL_DWEETS = "{0}{1}".format(BASE_URL, "get/dweets/for/{name}")

tempC = []

for i in range(0,26):
    tempC.append(0)

while True:

    ostemp = os.popen('vcgencmd measure_temp').readline()
    temp = (ostemp.replace("temp=", "").replace("'C\n", ""))
    #temp = 14
    print(temp)
    tempC.append(temp)
    tempC.pop(0)
    #resposta = latest_dweet("fla")

    rqsString = dweetEnvia+nome+'?'+var1+'='+str(temp)+'&'+var2+'='+str(valor)+'&'+var3+'='+str(val1)
   # rqsString2 = var2+'='+str(valor)
    #print(rqsString)
    enviaDweet = requests.get(rqsString)

   # recebeDweet = requests.post('https://dweet.io/get/lastest/dweet/for/fla')
    #print(recebeDweet.status_code)
    print(valor)

    resposta = requests.get(dweetRecebe).json()
    time.sleep(7)
    print ("Oi" + resposta)


    #A Class for using the Dweet.io servers for data communication between devices
#class Dweet(object):


    def dweet(self, data):
        """
        Make a dweet without a thing name.
        Assigns a random thing name which is returned
        in the response body.
        Returns a dict type.

        Parameter name is a string type.
        Parameter data is a dict type.
        Usage:

        data = {"foo": "bar"}

        is turned into:
        /dweet?foo=bar
        """
        #try:
        return requests.get(self.DWEET, params=data).json()
        #except requests.exceptions.ConnectionError:
            #raise e
    def dweet_by_name(self, name, data):
        """
        Make a dweet with a named thing.
        Returns a dict type.

        Parameter name is a string type.
        Parameter data is a dict type.

        Usage:

        data = {"foo": "bar"}

        is turned into:
        /{name}?foo=bar

        """
        #try:
        return requests.get(self.DWEET_BY_NAME.format(name=name),
                            params=data).json()
        #except requests.exceptions.ConnectionError, e:
            #raise e
    
     def all_dweets(self, name):
        """
        Get dweets in last 24 hours by thing name.
        Dweet limit currently is 500 dweets.
        Returns dict type.
        Parameter name is a string type.
        """
        #try:
        return requests.get(self.ALL_DWEETS.format(name=name)).json()
        #except requests.exceptions.ConnectionError, e:
           # raise e

