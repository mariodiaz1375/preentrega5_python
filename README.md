# Blog en Python

Este sistema es un pequeño blog de consola que permite ver publicaciones, buscarlas por título, filtrarlas por tag y validar si cada post cumple con una estructura correcta.

## ¿Qué hace el programa?

El programa muestra un menú con varias opciones:

1. Ver todos los posts disponibles.
2. Buscar publicaciones por título.
3. Filtrar publicaciones por etiqueta o tag.
4. Validar si cada post está bien armado.
5. Salir del programa.

La idea es simular un blog simple desde la terminal, usando datos predefinidos en memoria. No usa base de datos ni interfaz gráfica, sino una estructura de Python con listas y diccionarios.

## Cómo ejecutar el sistema

1. Abrir la terminal en la carpeta del proyecto.
2. Asegurarse de tener el entorno virtual activado.
3. Ejecutar el archivo principal:

```bash
python main.py
```

Si estás en Windows y el entorno virtual ya está creado, también podés correrlo desde la terminal con:

```bash
python main.py
```

La aplicación mostrará un menú para que elijas qué acción realizar.

## Cómo está organizada la carpeta

```text
entregable5/
├── main.py
├── README.md
└── blog/
    ├── __init__.py
    ├── datos.py
    ├── menu.py
    ├── operaciones.py
    └── validaciones.py
```

### Explicación rápida:

- `main.py`: es el archivo principal. Aquí se inicia el programa y se controla el flujo del menú.
- `README.md`: explica el proyecto y cómo usarlo.
- `blog/`: carpeta que contiene la lógica del blog.
- `blog/datos.py`: guarda los datos iniciales del blog, como los posts y las etiquetas.
- `blog/menu.py`: muestra el menú y captura la opción elegida por el usuario.
- `blog/operaciones.py`: contiene las acciones de listar, buscar y filtrar posts.
- `blog/validaciones.py`: verifica si cada publicación tiene los datos necesarios y válidos.
- `blog/__init__.py`: marca la carpeta como un paquete de Python.

## ¿Qué responsabilidad cumple cada módulo?

### `main.py`
Es el punto de entrada del programa. Se encarga de:

- importar las funciones necesarias,
- mostrar el menú,
- leer la opción del usuario,
- ejecutar la acción correcta y
- salir cuando se elige la opción de cierre.

### `blog/datos.py`
Aquí se almacenan los datos del blog. Define:

- el perfil del autor,
- los estados posibles de un post,
- la lista de publicaciones iniciales.

### `blog/menu.py`
Se encarga de presentar las opciones al usuario y de capturar la respuesta. También controla errores si el usuario ingresa algo que no sea un número.

### `blog/operaciones.py`
Incluye la lógica de negocio del blog:

- `listar_posts()`: muestra todos los posts válidos.
- `buscar_por_titulo()`: busca publicaciones por texto dentro del título.
- `filtrar_por_tag()`: muestra publicaciones que tienen una etiqueta específica.

### `blog/validaciones.py`
Verifica si cada post cumple con las reglas del proyecto. Por ejemplo:

- que tenga todas las claves obligatorias,
- que el título y contenido no estén vacíos,
- que el autor sea un diccionario con nombre,
- que los tags sean una lista,
- que el estado sea válido.

## ¿Qué archivo se debe ejecutar?

El archivo que se debe ejecutar es:

- `main.py`

Este es el archivo principal del sistema y desde allí se inicia toda la aplicación.
