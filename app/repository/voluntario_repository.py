from app.config.database import SessionLocal
from app.entity.voluntario import VoluntarioORM


class VoluntarioRepository:

    def __init__(self):
        self.db = SessionLocal()

    def create(self, voluntario: VoluntarioORM):

        self.db.add(voluntario)
        self.db.commit()

        return voluntario

    def get(self, voluntario_id):

        return self.db.query(
            VoluntarioORM
        ).filter_by(
            id=voluntario_id
        ).first()

    def get_all(self):

        return self.db.query(
            VoluntarioORM
        ).all()