from app.config.database import SessionLocal
from app.entity.voluntario import VoluntarioORM


class VoluntarioRepository:

    def create(self, voluntario):

        db = SessionLocal()

        db.add(voluntario)
        db.commit()
        db.refresh(voluntario)

        db.close()

        return voluntario

    def get(self, voluntario_id):

        db = SessionLocal()

        result = db.query(VoluntarioORM)\
            .filter_by(id=voluntario_id)\
            .first()

        db.close()
        return result

    def get_all(self):

        db = SessionLocal()

        result = db.query(VoluntarioORM).all()

        db.close()
        return result

    def update(self, voluntario):
        db = SessionLocal()

        voluntario_db = db.query(VoluntarioORM) \
            .filter_by(id=voluntario.id) \
            .first()

        if voluntario_db:
            voluntario_db.nombre = voluntario.nombre
            voluntario_db.telefono = voluntario.telefono
            voluntario_db.tipo = voluntario.tipo
            voluntario_db.estado = voluntario.estado

            db.commit()
            db.refresh(voluntario_db)

        db.close()

        return voluntario_db

    def delete(self, voluntario_id):

        db = SessionLocal()

        voluntario = db.query(VoluntarioORM) \
            .filter_by(id=voluntario_id) \
            .first()

        if voluntario:
            db.delete(voluntario)
            db.commit()

        db.close()

        return voluntario