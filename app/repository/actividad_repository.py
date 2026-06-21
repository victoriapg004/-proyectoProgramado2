from app.config.database import SessionLocal
from app.entity.actividad import ActividadORM


class ActividadRepository:

    def __init__(self):
        self.db = SessionLocal()

    def create(self, actividad):

        self.db.add(actividad)
        self.db.commit()

        return actividad

    def get(self, actividad_id):

        return self.db.query(
            ActividadORM
        ).filter_by(
            id=actividad_id
        ).first()

    def get_all(self):

        return self.db.query(
            ActividadORM
        ).all()