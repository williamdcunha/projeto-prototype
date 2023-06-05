import copy

class Protótipo:
     def clone(self):
         return copy.deepcopy(self)

class Produto(Protótipo):
     def __init__(self, nome, preco):
         self.nome = nome
         self.preco = preco

     def __str__(self):
         return f"Produto: {self.nome}, Preço: {self.preco}"

# Criação de um objeto inicial
produto_inicial = Produto("Produto Inicial", 100)

# Clonagem do objeto inicial
produto_clonado = produto_inicial.clone()
print(produto_clonado)

# Modificação do objeto clonado
produto_clonado.name = "Produto Clonado"
produto_clonado.price = 200
print(produto_clonado)