
class Endereco:

    def __init__(self, logradouro, numero, cep, bairro, cidade, estado, pais):
        self.logradouro = logradouro
        self.numero = numero
        self.cep = cep
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.pais = pais

    def __str__(self):
        return f'{self.logradouro},{self.numero},{self.cep},{self.bairro},{self.cidade},{self.estado},{self.pais}'


    def cadastro(end):
        
        with open('endereco.txt', 'a') as arquivo:
            arquivo.write(str(end))
        return arquivo

    def endereco_resumido(self):
        lista = []
        with open('endereco.txt', 'r') as arquivo:
            for linha in arquivo:
                linha_tratada = linha.strip()
                dados = linha_tratada.split(',')
                endereco = Endereco(dados[0], dados[1], dados[2], dados[3], dados[4], dados[5], dados[6])
                lista.append(endereco)
        return lista

    