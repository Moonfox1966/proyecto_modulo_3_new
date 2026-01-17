
# Módulo de interfaz por consola (UI).
## Contiene funciones simples para mostrar mensajes y pedir datos.

def mostrar_titulo() -> None:
    """Imprime el título del sistema."""
    print("Sistema de Gestión de Datos")


def pedir_nombre() -> str:
    """Solicita el nombre al usuario y lo retorna limpio."""
    nombre = input("Ingrese su nombre: ").strip()
    return nombre


def mostrar_bienvenida(nombre: str) -> None:
    """Muestra un saludo usando f-strings."""
    print(f"Bienvenido, {nombre}")