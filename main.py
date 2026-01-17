
# Sistema de gestión de datos
# Tipos de datos y sentencias básicas
# Sentencias condicionales


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
    # Pide edad hasta que sea válida (entero y rango)
    while True:
        texto = input("Ingrese edad (entero): ").strip()

        if not texto.isdigit():
            print("Error: debe ser un número entero.")
            continue  # vuelve a pedir

        edad = int(texto)

        if not es_edad_valida(edad):
            print("Error: edad fuera de rango (1 a 120).")
            continue  # vuelve a pedir

        return edad


def main() -> None:
    # Lista principal del sistema (múltiples registros)
    usuarios = []

    while True:
        mostrar_menu()
        opcion = pedir_opcion()

        if opcion == "0":
            print("Saliendo del sistema...")
            break  # termina el programa

        if opcion not in {"1", "2", "3", "4"}:
            print("Opción inválida.")
            continue  # vuelve al menú

        if opcion == "1":
            nombre = cargar_nombre()
            edad = cargar_edad_validada()
            tipo = cargar_tipo_usuario()

            usuario = crear_usuario(nombre, edad, tipo)
            agregar_usuario(usuarios, usuario)
            print("Usuario agregado.")

        elif opcion == "2":
            listar_usuarios(usuarios)

        elif opcion == "3":
            nombre = input("Nombre a buscar: ").strip()
            usuario = buscar_por_nombre(usuarios, nombre)
            if usuario is None:
                print("No encontrado.")
            else:
                print(
                    f"Encontrado: {usuario['nombre']} | {usuario['edad']} | "
                    f"{usuario['tipo']} | {usuario['categoria']}"
                )

        elif opcion == "4":
            nombre = input("Nombre a eliminar: ").strip()
            eliminado = eliminar_por_nombre(usuarios, nombre)
            if eliminado:
                print("Usuario eliminado.")
            else:
                print("No se pudo eliminar: no existe.")

    # Fin del programa


if __name__ == "__main__":
    main()