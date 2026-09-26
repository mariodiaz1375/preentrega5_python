from blog.modelos import Autor, Post, Blog
from blog.menu import mostrar_menu


if __name__ == "__main__":
    perfil_autor = {
    "nombre": "Mario Alberto Diaz",
    "bio": "Desarrollador web y cientifico de datos.",
    "especialidad": "Python, Django y SQL",
    "redes_sociales": ["@mario_dev", "@mario_python"]
    }
    autor = Autor(
        nombre=perfil_autor["nombre"],
        bio=perfil_autor["bio"],
        especialidad=perfil_autor["especialidad"],
        redes_sociales=perfil_autor["redes_sociales"]
    )
    blog = Blog(
        nombre="Mi Blog",
        descripcion="Un blog sobre programacion y tecnologia.",
    )
    ejecutando = True
    
    while ejecutando:
        opcion = mostrar_menu()

        if opcion is None:
            continue

        if opcion == 1:
            lista = blog.listar_posts()
            print("\n--- LISTA DE POSTS ---")
            for post in lista:
                print(post)

        elif opcion == 2:
            termino = input("\nIngrese el título o palabra a buscar: ")
            resultados = blog.buscar_por_titulo(termino)
            print(f"\n--- RESULTADOS DE BUSQUEDA PARA '{termino}' ---")
            for post in resultados:
                print(post)

        elif opcion == 3:
            tag = input("\nIngrese el tag a filtrar: ")
            resultados = blog.filtrar_por_tag(tag)
            print(f"\n--- POSTS CON EL TAG '{tag}' ---")
            for post in resultados:
                print(post)

        elif opcion == 4:
            print("\n--- CREAR NUEVO POST ---")
            post = Post(
                id=input("ID del post: "),
                titulo=input("Título del post: "),
                contenido=input("Contenido del post: "),
                autor=autor,
                tags=input("Tags del post (separados por comas): ").split(","),
                estado=input("Estado del post: ")
            )
            blog.agregar_post(post)
            blog.guardar_en_json("posts.json")
            print("Post guardado correctamente.")

        elif opcion == 5:
            print("\nSaliendo del programa. ¡Hasta luego!")
            ejecutando = False