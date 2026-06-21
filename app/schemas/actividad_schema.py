from pydantic import BaseModel


class ActividadSchema(BaseModel):
    id: str
    nombre: str
    fecha: str
    ubicacion: str
    capacidad_maxima: int

    class Config:
        from_attributes = True