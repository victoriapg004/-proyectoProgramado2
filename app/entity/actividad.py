from sqlalchemy import Column, String, Integer, Date
from app.config.database import Base


class ActividadORM(Base):

    __tablename__ = "actividades_tb"

    id = Column(String(45), primary_key=True)
    nombre = Column(String(100))
    fecha = Column(Date)
    ubicacion = Column(String(100))
    capacidad_maxima = Column(Integer)

    def __init__(self, id, nombre, fecha, ubicacion, capacidad_maxima):
        self.id = id
        self.nombre = nombre
        self.fecha = fecha
        self.ubicacion = ubicacion
        self.capacidad_maxima = capacidad_maxima