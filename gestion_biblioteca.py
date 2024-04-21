class Libro:
    def __init__(self, titulo, autor, publicacion, isbn):
        self.titulo = titulo
        self.autor = autor
        self.publicacion = publicacion
        self.isbn = isbn


class Biblioteca:
    def __init__(self):
        self.catalogo = {}

    def agregar_libro(self, libro):
        self.catalogo[libro.isbn] = libro

    def encontrar_libro(self, titulo):
        for isbn, libro in self.catalogo.items():
            if libro.titulo == titulo:
                return (f"Titulo: {libro.titulo}, Autor: {libro.autor}, Año de publicación: {libro.publicacion}, "
                        f"ISBN: {libro.isbn}")
        return "Libro no encontrado"


def main():
    catalago1 = Biblioteca()
    libro1 = Libro("Sol desnudo", "Isaac Asimov", "1954", "12345")
    catalago1.agregar_libro(libro1)
    libro_encontrado = catalago1.encontrar_libro("Sol desnudo")
    print(libro_encontrado)


if __name__ == "__main__":
    main()
