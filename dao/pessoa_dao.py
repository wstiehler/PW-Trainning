from dao.dao import Dao
from models.pessoa_model import PessoaModel

class PessoaDao(Dao):

    def __init__(self):
        nome_arquivo = 'pessoa.txt'
        # super() == classe mae (herança)
        # chama o construtor da classe mãe passando o valor para o parametro obrigatório
        super().__init__(nome_arquivo)
    
    def cadastrar(self, pessoa:PessoaModel):
        dado = f'{pessoa.nome},{pessoa.sobrenome},{pessoa.idade},{pessoa.sexo}'
        return super().cadastrar(dado)
    
    def ler(self):
        dados = super().ler()
        lista_pessoa = []
        for dado in dados:
            pessoa_dados = str(dado).split(';')
            pessoa = PessoaModel()
            pessoa.nome = pessoa_dados[0]
            pessoa.sobrenome = pessoa_dados[1]
            pessoa.idade = pessoa_dados[2]
            pessoa.sexo = pessoa_dados[3]
            lista_pessoa.append(pessoa)
        return lista_pessoa






dao1 = PessoaDao()
dao1.cadastrar()

