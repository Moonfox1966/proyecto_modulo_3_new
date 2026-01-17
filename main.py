# -------------------------------------------
# Sistema de gestión de datos (Módulo 3 New)
# Archivo: main.py
# Objetivo: Punto de entrada del sistema
# -------------------------------------------

from modulos.ui import mostrar_titulo, pedir_nombre, mostrar_bienvenida

def main() -> None:

    # Función principal del programa.
    mostrar_titulo()
    nombre = pedir_nombre()
    mostrar_bienvenida(nombre)


if __name__ == "__main__":
    main()