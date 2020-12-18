#Criando a classe e seus métodos
class Pessoa():

    def __init__(self, nome, cidade, telefone, email):
        self.nome = nome
        self.cidade = cidade
        self.telefone = telefone
        self.email = email
        print("Objeto criado")

    def __str__(self):
        return "O usuário " + self.nome + " vive na cidade de " + self.cidade

#Fazendo o chamado da classe com seus parâmetros
teste = Pessoa("Valter", "Uberaba", 98898778, "Valter@gmail.com")

#Por algum motivo o comando "str" não está funcionando no meu Pycharm, logo utilizei o print que funciona do mesmo jeito
print(teste)
