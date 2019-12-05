#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 18:08:12 2019

@author: audrey
"""

#print("bot: {}".format("Meu nome é chatbot"))

cerebro = {
        "Olá": "Olá, tudo bem?",
        "Tudo, e você?": "Estou bem, em que posso ajudar?",
        "Você pode me dizer seu nome?": "Meu nome é Bot",
        "Sair": "Até logo!"
}

#pipeline
def respond(entrada):
    saida = "Não sei responder"
    for estimulo, resposta in cerebro.items():
        if entrada == estimulo:
            saida = resposta    
    return saida

while True: 
    entrada = input("Audrey: ")
    saida = respond(entrada)
    print("Máquina: {}".format(saida))