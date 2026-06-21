from sqlalchemy import Column, String, Integer
from app.config.database import Base


class ParticipacionORM(Base):

    __tablename__ = "participaciones"

    id = Column(String(45), primary_key=True)
    voluntario_id = Column(String(45))
    actividad_id = Column(String(45))
    horas = Column(Integer)

    def __init__(self, id, voluntario_id, actividad_id, horas):

        self.id = id
        self.voluntario_id = voluntario_id
        self.actividad_id = actividad_id
        self.horas = horas