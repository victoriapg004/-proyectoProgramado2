from app.config.database import SessionLocal
from app.entity.participacion import ParticipacionORM


class ParticipacionRepository:

    def create(self, participacion):

        db = SessionLocal()

        db.add(participacion)
        db.commit()
        db.close()

        return participacion

    def get(self, participacion_id):

        db = SessionLocal()

        result = db.query(ParticipacionORM)\
            .filter_by(id=participacion_id)\
            .first()

        db.close()

        return result

    def get_all(self):

        db = SessionLocal()

        result = db.query(ParticipacionORM).all()

        db.close()

        return result

    def update(self, participacion):

        db = SessionLocal()

        participacion_db = db.query(ParticipacionORM) \
            .filter_by(id=participacion.id) \
            .first()

        if participacion_db:
            participacion_db.voluntario_id = participacion.voluntario_id
            participacion_db.actividad_id = participacion.actividad_id
            participacion_db.horas = participacion.horas

            db.commit()
            db.refresh(participacion_db)

        db.close()

        return participacion_db

    def delete(self, participacion_id):

        db = SessionLocal()

        participacion = db.query(ParticipacionORM) \
            .filter_by(id=participacion_id) \
            .first()

        if participacion:
            db.delete(participacion)
            db.commit()

        db.close()

        return participacion

