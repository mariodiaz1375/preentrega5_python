from .datos import estados_post

def validar_post(post):
    """
    Verifica que el post cumpla con las reglas de negocio.
    Retorna (True, "Válido") o (False, "Motivo del error").
    """
    if not isinstance(post, dict):
        return False, "El post no es un diccionario"

    # claves obligatorias
    claves_obligatorias = ["id", "titulo", "contenido", "autor", "tags", "estado"]
    for clave in claves_obligatorias:
        if clave not in post:
            return False, f"Falta la clave obligatoria '{clave}'"

    # validacion del título
    if not str(post.get("titulo")).strip():
        return False, "El título está vacío"

    # validacion del contenido
    if not str(post.get("contenido")).strip():
        return False, "El contenido está vacío"

    # validacion del autor
    autor = post.get("autor")
    if not isinstance(autor, dict):
        return False, "La clave 'autor' no es un diccionario"
    if "nombre" not in autor or not str(autor.get("nombre")).strip():
        return False, "El autor no contiene la clave 'nombre' válida"

    # validacion de tags
    if not isinstance(post.get("tags"), list):
        return False, "La clave 'tags' debe ser una lista"

    # validacion del estado
    if post.get("estado") not in estados_post:
        return False, f"El estado '{post.get('estado')}' no pertenece a los estados válidos"

    return True, "Válido"