# -----------------------------------------
# Validaciones y reglas de negocio simples.
# Lección 3 - Sentencias condicionales



def es_nombre_valido(nombre: str) -> bool:
    # Nombre válido si no está vacío.
    return len(nombre.strip()) > 0


def es_edad_valida(edad: int) -> bool:
    # Edad válida si está en un rango razonable (1 a 120).
    return 1 <= edad <= 120


def obtener_categoria_por_edad(edad: int) -> str:
    
    # Regla del documento:
    # - si edad > 60 => 'adulto mayor'
    # - en caso contrario => 'adulto'
    
    if edad > 60:
        return "adulto mayor"
    return "adulto"


def es_tipo_valido(tipo: str) -> bool:
    # Tipo válido si no está vacío.
    return len(tipo.strip()) > 0