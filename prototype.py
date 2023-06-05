import copy

class ShapePrototype:
    def clone(self):
        return copy.deepcopy(self)

    def get_info(self):
        pass

class Rectangle(ShapePrototype):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_info(self):
        return f"Rectangle: width={self.width}, height={self.height}"

class ShapeManager:
    def __init__(self):
        self.prototypes = {}

    def register_prototype(self, name, prototype):
        self.prototypes[name] = prototype

    def create_shape(self, name, **kwargs):
        if name in self.prototypes:
            prototype = self.prototypes[name]
            new_shape = prototype.clone()
            for key, value in kwargs.items():
                setattr(new_shape, key, value)
            return new_shape
        else:
            raise ValueError(f"Prototype '{name}' not registered")

# Criar um gerenciador de formas
manager = ShapeManager()

# Criar um retângulo protótipo
rectangle_prototype = Rectangle(10, 20)

# Registrar o retângulo protótipo no gerenciador
manager.register_prototype("rectangle", rectangle_prototype)

# Criar um novo retângulo clonando o protótipo e modificando sua largura
rectangle = manager.create_shape("rectangle", width=15)

# Exibir informações do retângulo
print(rectangle.get_info())
