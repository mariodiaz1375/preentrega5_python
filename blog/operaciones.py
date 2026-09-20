from .validaciones import validar_post

def listar_posts(lista):
    """Muestra la lista de publicaciones con un formato claro y seguro."""
    print("\n--- LISTA DE POSTS ---")
    if not lista:
        print("No hay posts disponibles para mostrar.")
        return

    for post in lista:
        es_valido, mensaje = validar_post(post)  # solo mostrar posts válido
        if es_valido:
            # acceso seguro mediante .get() o verificación de tipos
            titulo = post.get("titulo", "Sin título")
            autor = post.get("autor")
            
            # obtener el nombre de forma segura si autor es diccionario
            if isinstance(autor, dict):
                nombre_autor = autor.get("nombre", "Autor desconocido")
            else:
                nombre_autor = "Autor no válido"
                
            print(f"• Título: {titulo} | Autor: {nombre_autor}")
        else:
            print(f"• Post ID {post.get('id', 'Desconocido')} no válido: {mensaje}")


def buscar_por_titulo(lista, termino):
    """Busca y muestra publicaciones cuyo título contenga el término (case-insensitive)."""
    if not termino.strip():
        print("\n[ADVERTENCIA] El término de búsqueda no puede estar vacío.")
        return

    termino_lower = termino.lower()
    coincidencias = []

    for post in lista:
        titulo = post.get("titulo", "")
        if isinstance(titulo, str) and termino_lower in titulo.lower():
            coincidencias.append(post)

    print(f"\n--- RESULTADOS DE BUSQUEDA PARA '{termino}' ---")
    if coincidencias:
        listar_posts(coincidencias)
    else:
        print("No se encontraron publicaciones con ese término.")


def filtrar_por_tag(lista, tag):
    """Filtra y muestra publicaciones que contengan el tag indicado (case-insensitive)."""
    if not tag.strip():
        print("\n[ADVERTENCIA] El tag a buscar no puede estar vacio.")
        return

    tag_lower = tag.lower()
    coincidencias = []

    for post in lista:
        tags = post.get("tags", [])
        if isinstance(tags, list):
            # comprobar si el tag esta en la lista de tags (ignorando mayusculas/minusculas)
            tags_lower = [t.lower() for t in tags if isinstance(t, str)]
            if tag_lower in tags_lower:
                coincidencias.append(post)

    print(f"\n--- POSTS CON EL TAG '{tag}' ---")
    if coincidencias:
        listar_posts(coincidencias)
    else:
        print("No se encontraron publicaciones con ese tag.")