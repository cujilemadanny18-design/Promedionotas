from modelos.producto import Producto
from modelos.usuario import Usuario


class Restaurante:
    def __init__(self) -> None:
        # Lista para almacenar los productos
        self.productos: list[Producto] = []

        # Lista para almacenar los usuarios
        self.usuarios: list[Usuario] = []

    # ==============================
    # MÉTODOS PARA PRODUCTOS
    # ==============================

    def registrar_producto(self, producto: Producto) -> bool:
        """Registra un producto evitando códigos duplicados."""

        if self.buscar_producto(producto.codigo) is not None:
            return False

        self.productos.append(producto)
        return True

    def buscar_producto(self, codigo: str) -> Producto | None:
        """Busca un producto utilizando su código."""

        for producto in self.productos:
            if producto.codigo == codigo:
                return producto

        return None

    def actualizar_producto(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float
    ) -> bool:
        """Actualiza los datos de un producto existente."""

        producto = self.buscar_producto(codigo)

        if producto is None:
            return False

        producto.nombre = nombre
        producto.categoria = categoria
        producto.precio = precio

        return True

    def eliminar_producto(self, codigo: str) -> bool:
        """Elimina un producto mediante su código."""

        producto = self.buscar_producto(codigo)

        if producto is None:
            return False

        self.productos.remove(producto)
        return True

    def listar_productos(self) -> list[Producto]:
        """Devuelve la lista de productos."""

        return self.productos

    # ==============================
    # MÉTODOS PARA USUARIOS
    # ==============================

    def registrar_usuario(self, usuario: Usuario) -> bool:
        """Registra un usuario evitando identificaciones duplicadas."""

        if self.buscar_usuario(usuario.identificacion) is not None:
            return False

        self.usuarios.append(usuario)
        return True

    def buscar_usuario(self, identificacion: str) -> Usuario | None:
        """Busca un usuario mediante su identificación."""

        for usuario in self.usuarios:
            if usuario.identificacion == identificacion:
                return usuario

        return None

    def listar_usuarios(self) -> list[Usuario]:
        """Devuelve la lista de usuarios."""

        return self.usuarios

    # ==============================
    # CONJUNTO DE CATEGORÍAS
    # ==============================

    def obtener_categorias(self) -> set[str]:
        """Obtiene las categorías únicas de los productos."""

        categorias: set[str] = set()

        for producto in self.productos:
            categorias.add(producto.categoria)

        return categorias
