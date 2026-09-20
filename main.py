from blog.menu import mostrar_menu
from blog.datos import posts
from blog.operaciones import listar_posts, buscar_por_titulo, filtrar_por_tag
from blog.validaciones import validar_post

if __name__ == "__main__":
    ejecutando = True
    
    while ejecutando:
        opcion = mostrar_menu()

        if opcion is None:
            continue

        if opcion == 1:
            listar_posts(posts)

        elif opcion == 2:
            termino = input("\nIngrese el título o palabra a buscar: ")
            buscar_por_titulo(posts, termino)

        elif opcion == 3:
            tag = input("\nIngrese el tag a filtrar: ")
            filtrar_por_tag(posts, tag)

        elif opcion == 4:
            print("\n--- VALIDACIÓN DE POSTS ---")
            for post in posts:
                es_valido, mensaje = validar_post(post)
                if es_valido:
                    print(f"• Post ID {post.get('id', 'Desconocido')} es válido.")
                else:
                    print(f"• Post ID {post.get('id', 'Desconocido')} no válido: {mensaje}")

        elif opcion == 5:
            print("\nSaliendo del programa. ¡Hasta luego!")
            ejecutando = False