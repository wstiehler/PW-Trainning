
class PessoaModel:


    def __init__(self, nome, sobrenome, idade, sexo):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.sexo = sexo

    def cadastro(nome, sobrenome, idade, sexo):
        with open('db.txt', 'a') as arquivo:
            arquivo.write(f'{nome}, {sobrenome}, {idade}, {sexo}\n') 
        
        return arquivo
    

    def leitura():
        lista = []
        with open('db.txt', 'r') as arquivo:
            for pessoa in arquivo:
                linha_tratada = pessoa.strip()
                dados = linha_tratada.split(';')
                pessoa = {'nome':dados[0], 'sobrenome':dados[1], 'idade':dados[2], 'sexo':dados[3]}
                lista.append(pessoa)
        return lista

dicionario = {'nome': '', 'sobrenome': '', 'idade': 0, 'sexo':''}

nome = input('Digite o seu nome: ')
sobrenome = input('Digite o seu sobrenome: ')
idade = int(input('Digite a sua idade: '))
sexo = input('Digite o seu sexo: ')
    
