class Usuario:
    def __init__(
        self,
        identificacion: str,
        nombre: str,
        correo: str
    ) -> None:

        if not identificacion.strip():
            raise ValueError("La identificación no puede estar vacía.")

        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")

        if not correo.strip():
            raise ValueError("El correo no puede estar vacío.")

        self.identificacion = identificacion
        self.nombre = nombre
        self.correo = correo

    def to_dict(self) -> dict:
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "correo": self.correo
        }

    @classmethod
    def from_dict(cls, datos: dict) -> "Usuario":
        return cls(
            datos["identificacion"],
            datos["nombre"],
            datos["correo"]
        )

    def __str__(self) -> str:
        return (
            f"{self.identificacion} | "
            f"{self.nombre} | {self.correo}"
        )
