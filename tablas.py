from app.config.database import engine, Base

from app.entity.voluntario import VoluntarioORM
from app.entity.actividad import ActividadORM
from app.entity.participacion import ParticipacionORM

Base.metadata.create_all(bind=engine)

print("Tablas creadas")