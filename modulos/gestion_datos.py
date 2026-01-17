# modulos/gestion_datos.py
# Gestión de listas y diccionarios

from modulos.validaciones import obtener_categoria_por_edad

# Tupla: roles permitidos (inmutable)
ROLES = ("Admin", "Usuario", "Invitado")


def crear_usuario(nombre: str, edad: int, tipo: str, email: str) -> dict:
    # Crea un usuario como diccionario
    categoria = obtener_categoria_por_edad(edad)
    return {
        "nombre": nombre,
        "edad": edad,
        "tipo": tipo,
        "categoria": categoria,
        "email": email,
    }


def agregar_usuario(usuarios: list, correos: set, usuario: dict) -> bool:
    # Usa set para evitar correos duplicados
    email = usuario.get("email")

    if email in correos:
        return False

    usuarios.append(usuario)      # append()
    correos.add(email)
    return True


def listar_usuarios(usuarios: list) -> None:
    # Lista todos los usuarios
    if not usuarios:
        print("\n No hay usuarios registrados.")
        return

    print("\n--- LISTADO ---")
    for u in usuarios:
        print(
            f"- {u.get('nombre')} | {u.get('edad')} | "
            f"{u.get('tipo')} | {u.get('categoria')} | {u.get('email')}"
        )


def eliminar_por_email(usuarios: list, correos: set, email: str) -> bool:
    # Elimina usuario usando email
    for u in usuarios:
        if u.get("email") == email:
            usuarios.remove(u)     # remove()
            correos.remove(email)
            return True
    return False


def mostrar_claves_y_valores(usuario: dict) -> None:
    # Uso de keys() y values()
    print("Claves:", list(usuario.keys()))
    print("Valores:", list(usuario.values()))