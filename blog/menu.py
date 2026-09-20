
def mostrar_menu():
    """Muestra las opciones del menú y retorna la opción elegida por el usuario de forma segura."""
    print("\n" + "="*30)
    print("      MENU DEL BLOG")
    print("="*30)
    print("1. Ver todos los posts")
    print("2. Buscar por titulo")
    print("3. Filtrar por tag")
    print("4. Validar posts")
    print("5. Salir")
    print("="*30)
    
    try:
        opcion = int(input("Seleccione una opción (1-5): "))
        return opcion
    except ValueError:
        print("\n[ERROR] Debe ingresar un número entero válido.")
        return None