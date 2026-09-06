class Producto:
    def __init__(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float
    ) -> None:
        if not codigo.strip():
            raise ValueError("El código no puede estar vacío.")

        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")

        if not categoria.strip():
            raise ValueError("La categoría no puede estar vacía.")

        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")

        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    def to_dict(self) -> dict:
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio
        }

    @classmethod
    def from_dict(cls, datos: dict) -> "Producto":
        return cls(
            datos["codigo"],
            datos["nombre"],
            datos["categoria"],
            float(datos["precio"])
        )

    def __str__(self) -> str:
        return (
            f"{self.codigo} | {self.nombre} | "
            f"{self.categoria} | ${self.precio:.2f}"
        )
