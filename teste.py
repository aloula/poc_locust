# Locust test file
# -*- coding: utf-8 -*- 
# Usage: locust -f teste.py --host=https://api.agify.io
# Author: Loula - 2022/05/17

from csv import reader
from random import randint
from locust import FastHttpUser, task, between, events

# teste
class UserBehaviour(FastHttpUser):
    wait_time = between(1, 5)
    # será executado somente no setup
    @events.test_start.add_listener
    def on_test_start(environment, **kwargs):
        # carrega massa
        with open('nomes.csv', 'r') as f:
            global lista_nomes, tamanho_lista_nomes
            lista_nomes = []
            file_reader = reader(f)
            lista_nomes = list(file_reader)
            tamanho_lista_nomes = len(lista_nomes)
    
    # bate na API com peso 100%
    @task(100)
    def check_age(self):
        index = randint(0, tamanho_lista_nomes - 1) # para pegar um nome da lista aleatóriamente
        nome = lista_nomes[index][0]
        self.client.get("/?name=" + nome, name="check_age") 