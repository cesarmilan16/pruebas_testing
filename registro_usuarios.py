class RegistroUsuarios:
    def __init__(self):
        self.usuarios = []

    def registrar_usuario(self, nombre, email):
        self.usuarios.append({'nombre': nombre, 'email': email})

    def mostrar_usuarios(self):
        return self.usuarios


def main():
    # Creamos una instancia de la clase RegistroUsuarios
    registro = RegistroUsuarios()

    # Ejemplo de registro de usuarios
    registro.registrar_usuario("Juan", "juan@example.com")
    registro.registrar_usuario("María", "maria@example.com")
    registro.registrar_usuario("Pedro", "pedro@example.com")

    # Mostramos la lista de usuarios registrados
    print("Lista de usuarios registrados:")
    usuarios = registro.mostrar_usuarios()
    for usuario in usuarios:
        print(f"Nombre: {usuario['nombre']}, Email: {usuario['email']}")


if __name__ == "__main__":
    main()
