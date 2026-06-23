from sqlalchemy import Column, String
from app.config.database import Base


class VoluntarioORM(Base):

    __tablename__ = "voluntario_tb"

    id = Column(String(45), primary_key=True)
    nombre = Column(String(100))
    telefono = Column(String(20))
    tipo = Column(String(45))
    estado = Column(String(45))

    def __init__(self, id, nombre, telefono, tipo, estado):

        self.id = id
        self.nombre = nombre
        self.telefono = telefono
        self.tipo = tipo
        self.estado = estado