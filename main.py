# Sistema de gestión de datos
# Tipos de datos y sentencias básicas
# Sentencias condicionales
# Sistema de gestión de datos - estructuras de datos
# Sistema de gestión de datos - funciones

from modulos.menu import mostrar_menu, pedir_opcion
from modulos.datos_basicos import cargar_nombre, cargar_tipo_usuario
from modulos.validaciones import es_edad_valida
from modulos.gestion_datos import (
    crear_usuario,
    agregar_usuario,
    listar_usuarios,
    eliminar_por_email,
)
from modulos.funciones_utiles import (
    contar_usuarios,
    es_admin,
    mostrar_resumen,
)


def cargar_edad_validada() -> int:
    # Solicita edad válida usando funciones y condicionales
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
    # Solicita email
    return input("Ingrese email: ").strip().lower()


def main() -> None:
    usuarios = []
    correos = set()

    while True:
        mostrar_menu()
        opcion = pedir_opcion()

        if opcion == "5":
            break

        if opcion == "1":
            nombre = cargar_nombre()
            edad = cargar_edad_validada()
            tipo = cargar_tipo_usuario()
            email = cargar_email()

            usuario = crear_usuario(nombre, edad, tipo, email)
            agregado = agregar_usuario(usuarios, correos, usuario)

            if agregado:
                print("\n --- Usuario agregado:")
                mostrar_resumen(usuario)

                if es_admin(usuario):
                    print("Aviso: el usuario es administrador.")
            else:
                print("Error: email duplicado.")

        elif opcion == "2":
            listar_usuarios(usuarios)
            print("Total usuarios:", contar_usuarios(usuarios))

        elif opcion == "4":
            email = cargar_email()
            eliminado = eliminar_por_email(usuarios, correos, email)
            print("Eliminado." if eliminado else "No existe.")

        else:
            print("Opción no implementada.")

    print("Fin del sistema.")


if __name__ == "__main__":
    main()