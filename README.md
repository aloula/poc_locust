# PoC - Testes de Performance com Python e Locust

Scripts para testes de performance usando Python e framework Locust. 

### Visão geral

Os scripts de teste estão na pasta [teste](teste) e no script do Locust (.py) temos o código do teste. 

### Pré-requisitos:

- Python 3.8+: https://www.python.org/downloads/
- Locust 2.8+: https://docs.locust.io/en/stable/installation.html

### Instalação (instruções Debian/Ubuntu):

1 - Instale o Python 3.8+:
```
$ sudo apt update
$ sudo apt upgrade
$ sudo apt install python3 python3-venv
```

2 - Verifique a instalação:
```
$ python3 -V
Python 3.8.XX
```

3 - Normalmente o Linux já vem com a versão do Python 2.7.X. Para deixar a versão 3 como padrão, acrescente a linha abaixo no ~/.bashrc:  
alias python='python3'

4 - Teste o alias:
```
$ source ~/.bashrc
$ python -V
Python 3.8.XX
```

5 - Crie e ative o ambiente virtual do Python:
```
$ python -m venv .venv
$ source .venv/bin/activate
```

5 - Instale o Locust:
```
$ pip install locust
```


### Execução:

- Para execução do Locust com UI:
```
$ locust -f <arquivo_do_teste.py> --host=<endpoint>
```
- Exemplo:
```
$ locust -f locust -f teste.py --host=https://api.agify.io
```
- Acesse a interface em: <localhost:8089> 

- Para execução do Locust sem UI:
```
$ locust -f <arquivo_do_teste.py> --host=<endpoint> --headless -u 100 -r 10 -t 10m
```
- Exemplo simulando 100 usuários com subida de 10 usuários/s e 10 mins de teste:
```
$ locust -f teste.py --host=https://api.agify.io --headless -u 100 -r 10 -t 10m
```
