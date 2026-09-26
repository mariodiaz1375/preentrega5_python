from .validaciones import validar_post
import json
from .datos import estados_post, perfil_autor, posts


class Autor:
    def __init__(self, nombre, bio, especialidad, redes_sociales):
        self.nombre = nombre
        self.bio = bio
        self.especialidad = especialidad
        self.redes_sociales = redes_sociales

    def __str__(self):
        return f"{self.nombre} - {self.especialidad}"


class Post:
    def __init__(self, id, titulo, contenido, autor, tags, estado):
        if isinstance(autor, Autor):
            self.id = id
            self.titulo = titulo
            self.contenido = contenido
            self.autor = autor
            self.tags = tags
            self.estado = estado
        else:
            raise ValueError("El autor debe ser una instancia de la clase Autor.")

    def __str__(self):
        return f"{self.titulo} - {self.estado} | Autor: {self.autor.nombre}"

class Blog:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.posts = []

    def __str__(self):
        return f"{self.nombre} - {self.descripcion} - {len(self.posts)} posts"

    def agregar_post(self, post):
        es_valido, mensaje = validar_post({
            "id": post.id,
            "titulo": post.titulo,
            "contenido": post.contenido,
            "autor": {
                "nombre": post.autor.nombre,
                "bio": post.autor.bio,
                "especialidad": post.autor.especialidad,
                "redes_sociales": post.autor.redes_sociales
            },
            "tags": post.tags,
            "estado": post.estado
        })
        if isinstance(post, Post) and es_valido:
            self.posts.append(post)
        else:
            print(f"[ERROR] No se pudo agregar el post ID {post.id}: {mensaje}")
            raise ValueError("El objeto debe ser una instancia de la clase Post.")

    def listar_posts(self):
        posts = []
        with open('posts.json', 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
                for post_data in data:
                    autor_data = post_data.get("autor", {})
                    autor = Autor(
                        nombre=autor_data.get("nombre", "Autor desconocido"),
                        bio=autor_data.get("bio", ""),
                        especialidad=autor_data.get("especialidad", ""),
                        redes_sociales=autor_data.get("redes_sociales", [])
                    )
                    post = Post(
                        id=post_data.get("id"),
                        titulo=post_data.get("titulo"),
                        contenido=post_data.get("contenido"),
                        autor=autor,
                        tags=post_data.get("tags", []),
                        estado=post_data.get("estado")
                    )
                    posts.append(post)
            except json.JSONDecodeError:
                print("[ERROR] El archivo JSON está vacío o corrupto.")
        return posts

    def buscar_por_titulo(self, termino):
        return [post for post in self.posts if termino.lower() in post.titulo.lower()]

    def filtrar_por_tag(self, tag):
        return [post for post in self.posts if tag.lower() in (t.lower() for t in post.tags)]

    # def validar(self):
    #     resultados = []
    #     for post in self.posts:
    #         es_valido, mensaje = validar_post({
    #             "id": post.id,
    #             "titulo": post.titulo,
    #             "contenido": post.contenido,
    #             "autor": {
    #                 "nombre": post.autor.nombre,
    #                 "bio": post.autor.bio,
    #                 "especialidad": post.autor.especialidad,
    #                 "redes_sociales": post.autor.redes_sociales
    #             },
    #             "tags": post.tags,
    #             "estado": post.estado
    #         })
    #         resultados.append((post.id, es_valido, mensaje))
    #     return resultados

    def guardar_en_json(self, archivo):
        try:
            with open(archivo, 'r', encoding='utf-8') as f:
                posts_guardados = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            posts_guardados = []

        posts_guardados.extend([{
                "id": post.id,
                "titulo": post.titulo,
                "contenido": post.contenido,
                "autor": {
                    "nombre": post.autor.nombre,
                    "bio": post.autor.bio,
                    "especialidad": post.autor.especialidad,
                    "redes_sociales": post.autor.redes_sociales
                },
                "tags": post.tags,
                "estado": post.estado
            } for post in self.posts])

        with open(archivo, 'w', encoding='utf-8') as f:
            json.dump(posts_guardados, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    autor1 = Autor(
        nombre=perfil_autor["nombre"],
        bio=perfil_autor["bio"],
        especialidad=perfil_autor["especialidad"],
        redes_sociales=perfil_autor["redes_sociales"]
    )

    post1 = Post(
        id=1,
        titulo="Primeros pasos con Python",
        contenido="En este post veremos una introduccion a la sintaxis basica de Python.",
        autor=autor1,
        tags=["Python", "Principiantes"],
        estado=estados_post[1]
    )

    post2 = Post(
        id=2,
        titulo="Qué es Django",
        contenido="Django es un framework de desarrollo web de alto nivel escrito en Python.",
        autor=autor1,
        tags=["Python", "Django", "Web"],
        estado=estados_post[0]
    )

    post3 = Post(
        id=3,
        titulo="Organizando datos con diccionarios",
        contenido="Los diccionarios nos permiten guardar informacion mediante pares clave-valor.",
        autor=autor1,
        tags=["Python", "Diccionarios"],
        estado=estados_post[2]
    )

    post4 = Post(
        id=4,
        titulo="",
        contenido="Aprende a estructurar las vistas y modelos de tu blog.",
        autor=autor1,
        tags=[],
        estado=estados_post[0]
    )


    blog = Blog(
        nombre="Mi Blog",
        descripcion="Un blog sobre programacion y tecnologia.",
    )

    # blog.agregar_post(post1)
    # blog.agregar_post(post2)    
    # blog.agregar_post(post3)
    # print(post4.autor)
    # blog.agregar_post(post4)

    for post in blog.listar_posts():
        print(post)
    # for post in blog.buscar_por_titulo("Python"):
    #     print(post)