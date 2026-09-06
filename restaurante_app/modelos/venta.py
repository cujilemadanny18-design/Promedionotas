class Venta:
    def __init__(
        self,
        codigo_venta: str,
        identificacion_usuario: str,
        codigo_producto: str,
        cantidad: int,
        total: float
    ) -> None:

        if not codigo_venta.strip():
            raise ValueError("El código de venta no puede estar vacío.")

        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")

        if total <= 0:
            raise ValueError("El total debe ser mayor que cero.")

        self.codigo_venta = codigo_venta
        self.identificacion_usuario = identificacion_usuario
        self.codigo_producto = codigo_producto
        self.cantidad = cantidad
        self.total = total

    def to_dict(self) -> dict:
        return {
            "codigo_venta": self.codigo_venta,
            "identificacion_usuario": self.identificacion_usuario,
            "codigo_producto": self.codigo_producto,
            "cantidad": self.cantidad,
            "total": self.total
        }

    @classmethod
    def from_dict(cls, datos: dict) -> "Venta":
        return cls(
            datos["codigo_venta"],
            datos["identificacion_usuario"],
            datos["codigo_producto"],
            int(datos["cantidad"]),
            float(datos["total"])
        )

    def __str__(self) -> str:
        return (
            f"Venta: {self.codigo_venta} | "
            f"Usuario: {self.identificacion_usuario} | "
            f"Producto: {self.codigo_producto} | "
            f"Cantidad: {self.cantidad} | "
            f"Total: ${self.total:.2f}"
        )
