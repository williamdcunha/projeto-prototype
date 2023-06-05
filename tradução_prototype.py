import copy

class PrototipoForma:
    def clonar(self):
        return copy.deepcopy(self)

    def obter_informacoes(self):
        pass

class Retangulo(PrototipoForma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def obter_informacoes(self):
        return f"Retângulo: largura={self.largura}, altura={self.altura}"

class GerenciadorFormas:
    def __init__(self):
        self.prototipos = {}

    def registrar_prototipo(self, nome, prototipo):
        self.prototipos[nome] = prototipo

    def criar_forma(self, nome, **kwargs):
        if nome in self.prototipos:
            prototipo = self.prototipos[nome]
            nova_forma = prototipo.clonar()
            for chave, valor in kwargs.items():
                setattr(nova_forma, chave, valor)
            return nova_forma
        else:
            raise ValueError(f"Protótipo '{nome}' não está registrado")


#########################################################
##### EXPLICANDO O GERENCIADOR E CLONES NO TERMINAL #####
#########################################################

##### Criar um gerenciador de formas 
gerenciador_formas = GerenciadorFormas()

##### Criar um protótipo de retângulo
prototipo_retangulo = Retangulo(10, 20)

##### Será Registrado o protótipo de retângulo no gerenciador
gerenciador_formas.registrar_prototipo("retangulo", prototipo_retangulo)

##### O novo retângulo clonado >>>> e o protótipo modificando a largura
novo_retangulo = gerenciador_formas.criar_forma("retangulo", largura=15)


##### Aqui vai exibir as informações do retângulo e clone do novo
print("protótipos: ", prototipo_retangulo.obter_informacoes())

print("Novo retângulo: ", novo_retangulo.obter_informacoes())




