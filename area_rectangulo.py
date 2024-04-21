class Rectangulo:
    def __init__(self, longitud, anchura):
        self.longitud = longitud
        self.anchura = anchura

    def calcular_area(self):
        area = self.longitud * self.anchura
        return area

    def calcular_perimetro(self):
        perimetro = self.longitud * 2 + self.anchura * 2
        return perimetro


def main():
    rectangulo1 = Rectangulo(10, 5)
    area = rectangulo1.calcular_area()
    print("El area es: {}".format(area))
    perimetro = rectangulo1.calcular_perimetro()
    print("\nEl perimetro es: {}".format(perimetro))


if __name__ == "__main__":
    main()
