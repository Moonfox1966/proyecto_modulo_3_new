# modulos/menu.py
# Funciones del menú


def mostrar_menu() -> None:
    # Imprime opciones del sistema
    print("\n--- MENÚ ---")
    print("1) Agregar usuario")
    print("2) Listar usuarios")
    print("3) Buscar usuario por nombre")
    print("4) Eliminar usuario por nombre")
    print("5) Salir")


def pedir_opcion() -> str:
    # Pide opción como texto 
    return input("\n Seleccione una opción: ").strip()