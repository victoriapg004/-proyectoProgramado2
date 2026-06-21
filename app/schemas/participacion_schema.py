from pydantic import BaseModel


class ParticipacionSchema(BaseModel):
    id: str
    voluntario_id: str
    actividad_id: str
    horas: int

    class Config:
        from_attributes = True