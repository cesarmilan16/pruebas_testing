class Empleado:
    def __init__(self, nombre, apellido, salario, antiguedad):
        self.nombre = nombre
        self.apellido = apellido
        self.salario = salario
        self.antiguedad = antiguedad

    def calcular_salario_anual(self):
        bono = self.salario * 0.05 * self.antiguedad
        salario_anual = self.salario * 12 + bono
        return salario_anual


def main():
    empleado1 = Empleado("Juan", "Perez", 1000, 10)

    salario_anual = empleado1.calcular_salario_anual()
    print("El salario anual de " + empleado1.nombre + " es de: {}".format(salario_anual))


if __name__ == "__main__":
    main()
