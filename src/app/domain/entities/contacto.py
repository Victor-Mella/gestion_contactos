from pydantic import BaseModel, Field


class Contacto(BaseModel):
    id: int
    nombre: str
    numero: str = Field(..., description="Numero Internacional")
