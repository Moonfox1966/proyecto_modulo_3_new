
# Sistema de gestión de datos
# Tipos de datos y sentencias básicas
# Sentencias condicionales

from modulos.datos_basicos import (
    cargar_nombre,
    cargar_edad,
    cargar_tipo_usuario,
    crear_registro,
)

from modulos.validaciones import (
    es_edad_valida,
    obtener_categoria_por_edad,
)

def main() -> None:
    # Función principal.
    usuarios = []

    nombre = cargar_nombre()

    while True:
        edad = cargar_edad()

        # Validación condicional (error de entrada)
        if es_edad_valida(edad):
            break

        print("Error: edad fuera de rango (1 a 120).")

    tipo = cargar_tipo_usuario()
    categoria = obtener_categoria_por_edad(edad)

    usuario = crear_registro(nombre, edad, tipo, categoria)
    usuarios.append(usuario)

    print("\nUsuario registrado:")
    print(f"Nombre: {usuario['nombre']}")
    print(f"Edad: {usuario['edad']}")
    print(f"Tipo: {usuario['tipo']}")
    print(f"Categoría: {usuario['categoria']}")

    # Expresión booleana y lógica simple
    es_admin = usuario["tipo"].lower() == "admin"
    if es_admin and usuario["categoria"] == "adulto mayor":
        print("Aviso: Admin y Adulto Mayor (validación lógica anidada).")


if __name__ == "__main__":
    main()