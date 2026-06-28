from app.config.database import SessionLocal
from app.entity.actividad import ActividadORM


class ActividadRepository:

    def create(self, actividad):
        db = SessionLocal()
        db.add(actividad)
        db.commit()
        db.close()

        return actividad

    def get(self, actividad_id):

        db = SessionLocal()

        result = db.query(ActividadORM)\
            .filter_by(id=actividad_id)\
            .first()

        db.close()

        return result

    def get_all(self):

        db = SessionLocal()

        result = db.query(ActividadORM).all()

        db.close()

        return result

    def update(self, actividad):

        db = SessionLocal()

        actividad_db = db.query(ActividadORM) \
            .filter_by(id=actividad.id) \
            .first()

        if actividad_db:
            actividad_db.nombre = actividad.nombre
            actividad_db.fecha = actividad.fecha
            actividad_db.ubicacion = actividad.ubicacion
            actividad_db.capacidad_maxima = actividad.capacidad_maxima

            db.commit()
            db.refresh(actividad_db)

        db.close()

        return actividad_db

    def delete(self, actividad_id):

        db = SessionLocal()

        actividad = db.query(ActividadORM) \
            .filter_by(id=actividad_id) \
            .first()

        if actividad:
            db.delete(actividad)
            db.commit()

        db.close()

        return actividad

