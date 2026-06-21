from app.config.database import SessionLocal
from app.entity.participacion import ParticipacionORM


class ParticipacionRepository:

    def __init__(self):
        self.db = SessionLocal()

    def create(self, participacion):

        self.db.add(participacion)
        self.db.commit()

        return participacion

    def get(self, participacion_id):

        return self.db.query(
            ParticipacionORM
        ).filter_by(
            id=participacion_id
        ).first()

    def get_all(self):

        return self.db.query(
            ParticipacionORM
        ).all()