from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante


# ==========================================
# CONFIGURACIÓN DEL SISTEMA
# ==========================================

restaurante = Restaurante()

# Tupla: opciones estables del menú
OPCIONES_MENU: tuple[str, ...] = (
    "Registrar producto",
    "Buscar producto",
    "Actualizar producto",
    "Eliminar producto",
    "Listar productos",
    "Registrar usuario",
    "Listar usuarios",
    "Mostrar categorías",
    "Salir"
)

# Diccionario: relación entre número de opción y texto
MENU: dict[int, str] = {
    1: OPCIONES_MENU[0],
    2: OPCIONES_MENU[1],
    3: OPCIONES_MENU[2],
    4: OPCIONES_MENU[3],
    5: OPCIONES_MENU[4],
    6: OPCIONES_MENU[5],
    7: OPCIONES_MENU[6],
    8: OPCIONES_MENU[7],
    9: OPCIONES_MENU[8]
}


# ==========================================
# FUNCIONES DEL MENÚ
# ==========================================

def mostrar_menu() -> None:
    print("\n========================================")
    print("        SISTEMA DE RESTAURANTE")
    print("========================================")

    for numero, opcion in MENU.items():
        print(f"{numero}. {opcion}")

    print("========================================")


def registrar_producto() -> None:
    print("\n--- REGISTRAR PRODUCTO ---")

    codigo = input("Ingrese el código: ").strip()
    nombre = input("Ingrese el nombre: ").strip()
    categoria = input("Ingrese la categoría: ").strip()

    try:
        precio = float(input("Ingrese el precio: "))

        if precio <= 0:
            print("El precio debe ser mayor que cero.")
            return

    except ValueError:
        print("Error: el precio debe ser un número válido.")
        return

    if not codigo or not nombre or not categoria:
        print("Todos los campos son obligatorios.")
        return

    producto = Producto(
        codigo,
        nombre,
        categoria,
        precio
    )

    if restaurante.registrar_producto(producto):
        print("Producto registrado correctamente.")
    else:
        print("Error: ya existe un producto con ese código.")


def buscar_producto() -> None:
    print("\n--- BUSCAR PRODUCTO ---")

    codigo = input("Ingrese el código del producto: ").strip()

    producto = restaurante.buscar_producto(codigo)

    if producto is not None:
        print("\nProducto encontrado:")
        print(producto)
    else:
        print("No se encontró ningún producto con ese código.")


def actualizar_producto() -> None:
    print("\n--- ACTUALIZAR PRODUCTO ---")

    codigo = input("Ingrese el código del producto: ").strip()

    producto = restaurante.buscar_producto(codigo)

    if producto is None:
        print("No se encontró el producto.")
        return

    print(f"Producto actual: {producto}")

    nombre = input("Nuevo nombre: ").strip()
    categoria = input("Nueva categoría: ").strip()

    try:
        precio = float(input("Nuevo precio: "))

        if precio <= 0:
            print("El precio debe ser mayor que cero.")
            return

    except ValueError:
        print("Error: el precio debe ser un número válido.")
        return

    if not nombre or not categoria:
        print("Los campos no pueden estar vacíos.")
        return

    actualizado = restaurante.actualizar_producto(
        codigo,
        nombre,
        categoria,
        precio
    )

    if actualizado:
        print("Producto actualizado correctamente.")
    else:
        print("No fue posible actualizar el producto.")


def eliminar_producto() -> None:
    print("\n--- ELIMINAR PRODUCTO ---")

    codigo = input("Ingrese el código del producto: ").strip()

    producto = restaurante.buscar_producto(codigo)

    if producto is None:
        print("No se encontró el producto.")
        return

    print(f"Producto encontrado: {producto}")

    confirmacion = input(
        "¿Está seguro de eliminarlo? (s/n): "
    ).strip().lower()

    if confirmacion == "s":
        eliminado = restaurante.eliminar_producto(codigo)

        if eliminado:
            print("Producto eliminado correctamente.")
        else:
            print("No fue posible eliminar el producto.")
    else:
        print("Operación cancelada.")


def listar_productos() -> None:
    print("\n--- LISTA DE PRODUCTOS ---")

    productos = restaurante.listar_productos()

    if not productos:
        print("No existen productos registrados.")
        return

    for producto in productos:
        print(producto)


def registrar_usuario() -> None:
    print("\n--- REGISTRAR USUARIO ---")

    identificacion = input(
        "Ingrese la identificación: "
    ).strip()

    nombre = input(
        "Ingrese el nombre: "
    ).strip()

    correo = input(
        "Ingrese el correo: "
    ).strip()

    if not identificacion or not nombre or not correo:
        print("Todos los campos son obligatorios.")
        return

    usuario = Usuario(
        identificacion,
        nombre,
        correo
    )

    if restaurante.registrar_usuario(usuario):
        print("Usuario registrado correctamente.")
    else:
        print("Error: ya existe un usuario con esa identificación.")


def listar_usuarios() -> None:
    print("\n--- LISTA DE USUARIOS ---")

    usuarios = restaurante.listar_usuarios()

    if not usuarios:
        print("No existen usuarios registrados.")
        return

    for usuario in usuarios:
        print(usuario)


def mostrar_categorias() -> None:
    print("\n--- CATEGORÍAS DE PRODUCTOS ---")

    categorias = restaurante.obtener_categorias()

    if not categorias:
        print("No existen categorías registradas.")
        return

    for categoria in sorted(categorias):
        print(f"- {categoria}")


# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

def main() -> None:
    while True:
        mostrar_menu()

        try:
            opcion = int(input("Seleccione una opción: "))

        except ValueError:
            print("Error: debe ingresar un número.")
            continue

        if opcion == 1:
            registrar_producto()

        elif opcion == 2:
            buscar_producto()

        elif opcion == 3:
            actualizar_producto()

        elif opcion == 4:
            eliminar_producto()

        elif opcion == 5:
            listar_productos()

        elif opcion == 6:
            registrar_usuario()

        elif opcion == 7:
            listar_usuarios()

        elif opcion == 8:
            mostrar_categorias()

        elif opcion == 9:
            print("\nGracias por utilizar el sistema.")
            break

        else:
            print("Opción inválida. Seleccione una opción del 1 al 9.")


if __name__ == "__main__":
    main()
