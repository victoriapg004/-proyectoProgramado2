from datetime import datetime, date

from app.entity.voluntario import VoluntarioORM
from app.entity.actividad import ActividadORM
from app.entity.participacion import ParticipacionORM

from app.repository.voluntario_repository import VoluntarioRepository
from app.repository.actividad_repository import ActividadRepository
from app.repository.participacion_repository import ParticipacionRepository


class VoluntariadoService:

    def __init__(self):
        self.vol_repo = VoluntarioRepository()
        self.act_repo = ActividadRepository()
        self.part_repo = ParticipacionRepository()

    # ---------------- VOLUNTARIOS ----------------

    def register_voluntario(self, id, nombre, telefono, tipo, estado):

        if not id.strip():
            raise ValueError("El ID no puede estar vacío")

        if self.vol_repo.get(id):
            raise ValueError("Ya existe un voluntario con ese ID")

        if not nombre.strip():
            raise ValueError("Nombre requerido")

        if not telefono.strip():
            raise ValueError("Teléfono requerido")

        voluntario = VoluntarioORM(
            id=id,
            nombre=nombre,
            telefono=telefono,
            tipo=tipo,
            estado=estado
        )

        return self.vol_repo.create(voluntario)

    def get_voluntarios(self):
        return self.vol_repo.get_all()

    def update_voluntario(self, id, nombre, telefono, tipo, estado):

        voluntario = VoluntarioORM(
            id=id,
            nombre=nombre,
            telefono=telefono,
            tipo=tipo,
            estado=estado
        )

        return self.vol_repo.update(voluntario)

    def delete_voluntario(self, voluntario_id):

        return self.vol_repo.delete(voluntario_id)

    # ---------------- ACTIVIDADES ----------------

    def register_actividad(self, id, nombre, fecha, ubicacion, capacidad_maxima):

        if self.act_repo.get(id):
            raise ValueError("Ya existe una actividad con ese ID")

        if not ubicacion.strip():
            raise ValueError("Ubicación requerida")

        capacidad_maxima = int(capacidad_maxima)


        if isinstance(fecha, str):
            fecha = datetime.strptime(fecha, "%Y-%m-%d").date()

        if fecha < date.today():
            raise ValueError("La fecha no puede ser anterior al día actual")

        actividad = ActividadORM(
            id=id,
            nombre=nombre,
            fecha=fecha,
            ubicacion=ubicacion,
            capacidad_maxima=capacidad_maxima
        )

        return self.act_repo.create(actividad)

    def get_actividades(self):
        return self.act_repo.get_all()

    def update_actividad(self, id, nombre, fecha, ubicacion, capacidad_maxima):

        actividad = ActividadORM(
            id=id,
            nombre=nombre,
            fecha=fecha,
            ubicacion=ubicacion,
            capacidad_maxima=capacidad_maxima
        )

        return self.act_repo.update(actividad)

    def delete_actividad(self, actividad_id):

        return self.act_repo.delete(actividad_id)

    # ---------------- PARTICIPACIONES ----------------

    def register_participacion(self, id, voluntario_id, actividad_id, horas):


        if not id.strip():
            raise ValueError("El ID es obligatorio")

        if self.part_repo.get(id):
            raise ValueError("Ya existe una participación con ese ID")

        voluntario = self.vol_repo.get(voluntario_id)
        if not voluntario:
            raise ValueError("El voluntario no existe")

        actividad = self.act_repo.get(actividad_id)
        if not actividad:
            raise ValueError("La actividad no existe")

        horas = int(horas)

        if horas <= 0 or horas > 24:
            raise ValueError("Horas inválidas")


        participantes = 0
        for p in self.part_repo.get_all():
            if p.actividad_id == actividad_id:
                participantes += 1

        if participantes >= actividad.capacidad_maxima:
            raise ValueError("Actividad llena")

        participacion = ParticipacionORM(
            id=id,
            voluntario_id=voluntario_id,
            actividad_id=actividad_id,
            horas=horas
        )

        actividad.capacidad_maxima -= 1
        self.act_repo.update(actividad)

        return self.part_repo.create(participacion)

    def get_participaciones(self):
        return self.part_repo.get_all()

    def update_participacion(self, id, voluntario_id, actividad_id, horas):

        participacion = ParticipacionORM(
            id=id,
            voluntario_id=voluntario_id,
            actividad_id=actividad_id,
            horas=horas
        )

        return self.part_repo.update(participacion)

    def delete_participacion(self, participacion_id):

        return self.part_repo.delete(participacion_id)

    # ---------------- REPORTES ----------------

    def voluntario_mas_horas(self):

        acumulado = {}

        for p in self.part_repo.get_all():
            acumulado[p.voluntario_id] = acumulado.get(p.voluntario_id, 0) + p.horas

        if not acumulado:
            return None

        mejor_id = max(acumulado, key=acumulado.get)
        voluntario = self.vol_repo.get(mejor_id)

        return {
            "nombre": voluntario.nombre,
            "horas": acumulado[mejor_id]
        }

    def actividad_mas_participacion(self):

        conteo = {}

        for p in self.part_repo.get_all():
            conteo[p.actividad_id] = conteo.get(p.actividad_id, 0) + 1

        if not conteo:
            return None

        mejor_id = max(conteo, key=conteo.get)
        actividad = self.act_repo.get(mejor_id)

        return {
            "actividad": actividad.nombre,
            "participaciones": conteo[mejor_id]
        }

    def cantidad_voluntarios_activos(self):

        total = 0

        for v in self.vol_repo.get_all():
            if v.estado.lower() == "activo":
                total += 1

        return {
            "activos": total
        }