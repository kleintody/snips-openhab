# -*- coding: utf-8 -*-
import toml
from hermes_python.hermes import Hermes
from hermes_python.ontology import MqttOptions
from hermes_python.ontology.injection import InjectionRequestMessage, AddFromVanillaInjectionRequest
from hermes_python.ontology.tts import RegisterSoundMessage
from os import environ, path

from hermes_python.hermes import Hermes
from hermes_python.ontology.injection import InjectionRequestMessage, AddInjectionRequest, AddFromVanillaInjectionRequest

# First example : We just add weekly releases

operations =  [
    AddFromVanillaInjectionRequest({"openhab/device" :  ["Couchlampe","Esstischlampe","Herdlampe","Spüllampe","Abwaschlampe"] }),
]

request1 = InjectionRequestMessage(operations)

with Hermes("localhost:1883") as h:
    h.request_injection(request1)


# Second example : We reset all the previously injected values of the book_title entity, and then, adds the list of values provided

#operations =  [
#i    AddFromVanillaInjectionRequest({"book_titles" : retrieve_book_inventory() }),
#]
#
#request2 = InjectionRequestMessage(operations)
#
#with Hermes("localhost:1883") as h:
#    h.request_injection(request2)
