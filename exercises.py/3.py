# Desenvolva uma classe Rectangle com atributos width e height.
# Implemente um método calculate_area para calcular e retornar a área do retângulo.

class Rectangle:
    def __init__(self, width, heigth):
        self.width = width
        self.heigth = heigth
    def calcule_area(self, calculo):
        self.calculo = calculo
        calculo = self.width*self.heigth
        return calculo

area = Rectangle(10, 10)
print(area.calcule_area(any)) # Vê sobre o parâmetro "any"