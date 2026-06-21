from pydantic import BaseModel


class VoluntarioSchema(BaseModel):
    id: str
    nombre: str
    telefono: str
    tipo: str
    estado: str

    class Config:
        from_attributes = True