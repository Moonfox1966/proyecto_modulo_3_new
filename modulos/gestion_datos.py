# modulos/gestion_datos.py
# Gestión de listas y diccionarios

from modulos.validaciones import obtener_categoria_por_edad


def crear_usuario(nombre: str, edad: int, tipo: str) -> dict:
    # Crea un usuario como diccionario
    categoria = obtener_categoria_por_edad(edad)
    return {"nombre": nombre, "edad": edad, "tipo": tipo, "categoria": categoria}


def agregar_usuario(usuarios: list, usuario: dict) -> None:
    # Agrega un usuario a la lista
    usuarios.append(usuario)


def listar_usuarios(usuarios: list) -> None:
    # Muestra todos los usuarios
    if len(usuarios) == 0:
        print("No hay usuarios registrados.")
        return

    print("\n--- LISTADO ---")
    for u in usuarios:
        print(f"- {u['nombre']} | {u['edad']} | {u['tipo']} | {u['categoria']}")


def buscar_por_nombre(usuarios: list, nombre: str) -> dict | None:
    # Busca el primer usuario que coincida por nombre (ignorando mayúsculas)
    nombre = nombre.strip().lower()
    for u in usuarios:
        if u["nombre"].strip().lower() == nombre:
            return u
    return None


def eliminar_por_nombre(usuarios: list, nombre: str) -> bool:
    # Elimina el primer usuario que coincida por nombre
    usuario = buscar_por_nombre(usuarios, nombre)
    if usuario is None:
        return False

    usuarios.remove(usuario)
    return True