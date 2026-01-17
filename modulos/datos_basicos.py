# -------------------------------------------
# Funciones de carga de datos básicos del usuario.
# Tipos de datos y sentencias básicas
# Tipos de datos y condicionales
# -------------------------------------------

from modulos.validaciones import es_nombre_valido, es_tipo_valido

def cargar_nombre() -> str:
    #Solicita y retorna el nombre validado.
    while True:
        nombre = input("Ingrese nombre: ").strip()
        if es_nombre_valido(nombre):
            return nombre
        print("Error: nombre no válido.")


def cargar_tipo_usuario() -> str:
    # Solicita y retorna el tipo validado.
    while True:
        tipo = input("Ingrese tipo de usuario: ").strip()
        if es_tipo_valido(tipo):
            return tipo
        print("Error: tipo no válido.")


def crear_registro(nombre: str, edad: int, tipo: str, categoria: str) -> dict:
    # Crea un registro de usuario como diccionario.
    return {
        "nombre": nombre,
        "edad": edad,
        "tipo": tipo,
        "categoria": categoria,
    }


def cargar_edad() -> int:
    
    # Solicita edad como entero usando solo condicionales.
    while True:
        texto = input("Ingrese edad (entero): ").strip()

        if not texto.isdigit():
            print("Error: debe ser un número entero.")
            continue

        edad = int(texto)
        return edad