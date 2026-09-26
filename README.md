# Blog en Python orientado a objetos

Este proyecto es un sistema de blog de consola desarrollado con programación orientada a objetos en Python. La lógica principal está organizada en clases que representan al autor, a cada publicación y al propio blog.

## ¿Qué hace el programa?

El programa permite:

1. Ver todos los posts del blog.
2. Buscar publicaciones por título.
3. Filtrar publicaciones por tag.
4. Crear un nuevo post desde la consola.
5. Guardar los posts en un archivo JSON.
6. Salir del programa.

La aplicación se ejecuta desde la terminal y ofrece un menú interactivo para que el usuario seleccione acciones sobre la colección de publicaciones.

## Arquitectura orientada a objetos

El sistema está modelado con estas clases:

### `Autor`
Representa al autor del blog. Tiene atributos como:

- nombre
- bio
- especialidad
- redes_sociales

Se encarga de describir la identidad del creador de las publicaciones.

### `Post`
Representa una publicación del blog. Tiene atributos como:

- id
- titulo
- contenido
- autor
- tags
- estado

Además, valida que el autor sea una instancia de la clase `Autor` antes de crear el objeto.

### `Blog`
Representa el conjunto completo de publicaciones. Tiene:

- nombre
- descripcion
- posts

Incluye métodos para:

- agregar_post(post)
- listar_posts()
- buscar_por_titulo(termino)
- filtrar_por_tag(tag)
- guardar_en_json(archivo)

## Flujo principal del programa

El archivo `main.py` crea una instancia de `Autor` y una instancia de `Blog`, y luego entra en un bucle mientras el usuario interactúa con el menú.

La lógica es la siguiente:

- Se crea el perfil del autor.
- Se crea el blog con un nombre y una descripción.
- Se muestra el menú.
- Según la opción elegida, se ejecuta una acción:
  - listados,
  - búsquedas,
  - filtros,
  - creación de nuevos posts.
- Cuando se crea un nuevo post, se valida y luego se guarda en `posts.json`.

## Validaciones del sistema

La validación de los datos se realiza con la función `validar_post()` en el módulo `blog/validaciones.py`.

Se comprueba que: 

- el post sea un diccionario válido,
- tenga todas las claves obligatorias,
- el título no esté vacío,
- el contenido no esté vacío,
- el autor sea un diccionario con nombre válido,
- los tags sean una lista,
- el estado pertenezca a los valores permitidos.

Esto ayuda a evitar publicaciones incompletas o inconsistentes.

## Estructura del proyecto

```text
entregable5/
├── main.py
├── posts.json
├── README.md
└── blog/
    ├── __init__.py
    ├── datos.py
    ├── menu.py
    ├── modelos.py
    ├── operaciones.py
    └── validaciones.py
```

## Descripción de cada módulo

### `main.py`
Es el punto de entrada de la aplicación. Aquí se instancian los objetos y se ejecuta el menú principal.

### `blog/datos.py`
Define los datos base del sistema, como:

- perfil del autor,
- estados posibles del post,
- lista inicial de publicaciones.

### `blog/menu.py`
Muestra el menú al usuario y captura la opción ingresada por consola.

### `blog/modelos.py`
Contiene las clases principales del sistema: `Autor`, `Post` y `Blog`.

### `blog/operaciones.py`
Mantiene funciones de apoyo para mostrar listas, búsquedas y filtros. Aunque el sistema actual se centra en la clase `Blog`, este módulo sigue representando la lógica de operaciones del blog en formato funcional.

### `blog/validaciones.py`
Valida que cada publicación tenga la estructura correcta antes de agregarse al blog.

## Cómo ejecutar el proyecto

Desde la raíz del proyecto, ejecutá:

```bash
python main.py
```

Luego se mostrará el menú del blog en la consola y podrás interactuar con el sistema.

## Persistencia

Los posts creados por el usuario se guardan en el archivo `posts.json` utilizando `json.dump()`. Así, la información del blog puede conservarse entre ejecuciones.

## Resumen

La versión actual del blog ya no trabaja solo con listas y diccionarios sueltos, sino que usa una estructura orientada a objetos para encapsular mejor la lógica del dominio. Esto hace que el código sea más claro, mantenible y reutilizable.
