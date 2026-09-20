perfil_autor = {
    "nombre": "Mario Alberto Diaz",
    "bio": "Desarrollador web y cientifico de datos.",
    "especialidad": "Python, Django y SQL",
    "redes_sociales": ["@mario_dev", "@mario_python"]
}

estados_post = ("borrador", "publicado", "archivado")

etiquetas_blog = {"SQL", "Django", "Web", "Backend", "Python", "SQL"}

posts = [
    {
        "id": 1,
        "titulo": "Primeros pasos con Python",
        "contenido": "En este post veremos una introduccion a la sintaxis basica de Python.",
        "autor": perfil_autor,
        "tags": ["Python", "Principiantes"],
        "estado": estados_post[1]
    },
    {
        "id": 2,
        "titulo": "Qué es Django",
        "contenido": "Django es un framework de desarrollo web de alto nivel escrito en Python.",
        "autor": perfil_autor,
        "tags": ["Python", "Django", "Web"],
        "estado": estados_post[0]
    },
    {
        "id": 3,
        "titulo": "Organizando datos con diccionarios",
        "contenido": "Los diccionarios nos permiten guardar informacion mediante pares clave-valor.",
        "autor": perfil_autor,
        "tags": ["Python", "Diccionarios"],
        "estado": estados_post[2]
    },
    {
        "id": 4,
        "titulo": "Creando un blog con Django",
        "contenido": "Aprende a estructurar las vistas y modelos de tu blog.",
        "autor": perfil_autor,
        "tags": ["Python", "Django", "Web"],
        "estado": estados_post[1]
    },
    # post incompleto/incorrecto agregando intencionalmente para probar la validación
    {
        "id": 5,
        "titulo": "",  # titulo vacío
        # falta la clave "contenido"
        "autor": "Mario Diaz",  # no es un diccionario
        "tags": "Python",  # deberia ser una lista, no un string
        "estado": "invalido"  # estado no perteneciente a estados_post
    }
]