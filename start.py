import sys, os
sys.path.append(os.getcwd)
from pprint import pprint
from models.exemplo2 import Endereco

# logradouro = input('Informe o logradouro: ')
# numero = input('Informe o numero: ')
# cep = input('Informe o cep: ')
# bairro = input('Informe o bairro: ')
# cidade = input('Informe o cidade: ')
# estado = input('Informe o estado: ')
# pais = input('Informe o pais: ')

# endereco = Endereco(logradouro, numero, cep, bairro, cidade, estado, pais)
# endereco.cadastro()
# lista = endereco.endereco_resumido()
# for endereco in lista:
#     print(endereco)


from models.pessoa_model import PessoaModel
from dao.pessoa_dao import PessoaDao

pessoa1 = PessoaModel()
pessoa1.nome = 'Will'
pessoa1.sobrenome = 'Villani Stiehler'
pessoa1.idade = 20
pessoa1.sexo = 'Masculino'

pessoa_dao = PessoaDao()
pessoa_dao.cadastrar()