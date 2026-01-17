# Sistema de gestión de datos
# Tipos de datos y sentencias básicas
# Sentencias condicionales
# Sistema de gestión de datos estructuras de datos

from modulos.menu import mostrar_menu, pedir_opcion
from modulos.datos_basicos import cargar_nombre, cargar_tipo_usuario
from modulos.validaciones import es_edad_valida
from modulos.gestion_datos import (
    crear_usuario,
    agregar_usuario,
    listar_usuarios,
    eliminar_por_email,
    mostrar_claves_y_valores,
)


def cargar_edad_validada() -> int:
    # Pide edad válida
    while True:
        texto = input("Ingrese edad (entero): ").strip()

        if not texto.isdigit():
            print("Error: debe ser entero.")
            continue

        edad = int(texto)

        if not es_edad_valida(edad):
            print("Error: edad fuera de rango.")
            continue

        return edad


def cargar_email() -> str:
    # Solicita email simple
    return input("Ingrese email: ").strip().lower()


def main() -> None:
    usuarios = []      # lista
    correos = set()    # set para emails únicos

    while True:
        mostrar_menu()
        opcion = pedir_opcion()

        if opcion == "0":
            break

        if opcion == "1":
            nombre = cargar_nombre()
            edad = cargar_edad_validada()
            tipo = cargar_tipo_usuario()
            email = cargar_email()

            usuario = crear_usuario(nombre, edad, tipo, email)
            agregado = agregar_usuario(usuarios, correos, usuario)

            if agregado:
                print("Usuario agregado.")
                mostrar_claves_y_valores(usuario)
            else:
                print("Error: email duplicado.")

        elif opcion == "2":
            listar_usuarios(usuarios)

        elif opcion == "4":
            email = cargar_email()
            eliminado = eliminar_por_email(usuarios, correos, email)
            print("Eliminado." if eliminado else "No existe.")

        else:
            print("Opción no implementada en esta lección.")


if __name__ == "__main__":
    main()