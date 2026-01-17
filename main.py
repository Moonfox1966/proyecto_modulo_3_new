"""
Sistema de gestión de datos
Lección 2 - Tipos de datos y sentencias básicas
"""

from modulos.datos_basicos import (
    cargar_nombre,
    cargar_edad,
    cargar_tipo_usuario,
    crear_registro,
)


def main() -> None:
    #Función principal.
    usuarios = []  # lista de diccionarios

    nombre = cargar_nombre()
    edad = cargar_edad()
    tipo = cargar_tipo_usuario()

    usuario = crear_registro(nombre, edad, tipo)
    usuarios.append(usuario)

    print("\nUsuario registrado:")
    print(f"Nombre: {usuario['nombre']}")
    print(f"Edad: {usuario['edad']}")
    print(f"Tipo: {usuario['tipo']}")

    print("\nTotal de usuarios registrados:", len(usuarios))


if __name__ == "__main__":
    main()