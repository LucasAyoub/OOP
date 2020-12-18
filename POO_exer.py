#Criando a classe e definindo seus métodos
class smartphone():

    def __init__(self, tamanho, interface):
        self.interface = interface
        self.tamanho = tamanho
        print("Objeto criado com sucesso")

#Criando a herança/sub-classe e definindo seus métodos mantendo a da classe mãe/super-classe
class mp3player(smartphone):

    def __init__(self, capacidade, tamanho="pequeno", interface="led"):
        smartphone.__init__(self, tamanho, interface)
        self.capacidade = capacidade
        print("Objeto mp3player criado")

    def print_mp3(self):
        print("Valores do objeto criado: %s, %s, %s" % (self.tamanho, self.interface, self.capacidade))

#Fazendo o chamado da classe e a imprimindo
blackberry = mp3player("64 gb")
blackberry.print_mp3()