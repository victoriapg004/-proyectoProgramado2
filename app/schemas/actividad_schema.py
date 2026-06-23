from pydantic import BaseModel
from datetime import date


class ActividadSchema(BaseModel):
    id: str
    nombre: str
    fecha: date
    ubicacion: str
    capacidad_maxima: int

    class Config:
        from_attributes = True