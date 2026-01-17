# -------------------------------------------
# Funciones de carga de datos básicos del usuario.
# Tipos de datos y sentencias básicas
# -------------------------------------------


def cargar_nombre() -> str:
    #Solicita y retorna el nombre del usuario.
    return input("Ingrese nombre: ").strip()


def cargar_edad() -> int:
    #Solicita edad y la convierte a entero.
    return int(input("Ingrese edad: "))


def cargar_tipo_usuario() -> str:
    #Solicita el tipo de usuario.
    return input("Ingrese tipo de usuario: ").strip()


def crear_registro(nombre: str, edad: int, tipo: str) -> dict:
    #Crea un registro de usuario como diccionario.
    return {
        "nombre": nombre,
        "edad": edad,
        "tipo": tipo,
    }