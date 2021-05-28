
class Dao:

    #Método construtor, sempre chamado ao criar um objeto da classe. 
    def __init__(self, nome_arquivo) -> None:
        self.arquivo = nome_arquivo

    def cadastrar(self, dado):
        with open(self.arquivo, 'a') as arquivo:
            arquivo.write(f'{dado}\n')

    def ler(self):
        with open(self.arquivo, 'r') as arquivo:
            lista = []
            for linha in arquivo:
                dado = linha.strip()
                lista.append(dado)
        return lista

    def reescrever_arquivo(self, novos_dados):
        with open(self.arquivo, 'w') as arquivo:
            for dado in novos_dados:
                arquivo.write(f'{dado}\n')

    def alterar(self, valor_antigo, novo_valor):
        #buscar o dado no arquivo
        lista_dados = self.ler()
        novos_dados = []
        #Percorrendo a lista para verificar se existe correspondencia do valor passado(valor_antigo)
        for dado in lista_dados:
            #Se o dado do arquivo for igual ao dado informado por parametro, subistitui pelo novo valor
            if dado == valor_antigo:
                dado = novo_valor
            novos_dados.append(dado)
            self.reescrever_arquivo(novos_dados)

        #reescrever o novo conteudo

    def excluir(self, dado):
        lista_de_dados = self.ler()
        novos_dados = []

        for linha in lista_de_dados:
            if linha != dado:
                novos_dados.append(dado)
            self.reescrever_arquivo(novos_dados)

dao1 = Dao('pessoa.txt')
dao1.cadastrar('valor antigo')
print(dao1.ler())
dao1.alterar('valor antigo', 'novo valor')
print(dao1.ler())
print(dao1.excluir('novo valor'))

