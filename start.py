import sys, os
sys.path.append(os.getcwd)
from pprint import pprint
from models.exemplo2 import Endereco



logradouro = input('Informe o logradouro: ')
numero = input('Informe o numero: ')
cep = input('Informe o cep: ')
bairro = input('Informe o bairro: ')
cidade = input('Informe o cidade: ')
estado = input('Informe o estado: ')
pais = input('Informe o pais: ')

endereco = Endereco(logradouro, numero, cep, bairro, cidade, estado, pais)
endereco.cadastro()
pprint(endereco.endereco_resumido())
