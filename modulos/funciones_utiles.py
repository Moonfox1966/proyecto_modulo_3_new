# modulos/funciones_utiles.py
# Funciones reutilizables del sistema


def contar_usuarios(usuarios: list) -> int:
    # Retorna la cantidad total de usuarios
    return len(usuarios)


def es_admin(usuario: dict) -> bool:
    # Retorna True si el usuario es admin
    return usuario.get("tipo", "").lower() == "admin"


def mostrar_resumen(usuario: dict) -> None:
    # Muestra un resumen del usuario
    print(
        f"{usuario.get('nombre')} | "
        f"{usuario.get('edad')} | "
        f"{usuario.get('tipo')} | "
        f"{usuario.get('categoria')}"
    )