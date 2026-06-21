from datetime import datetime

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

    # ---------------- ACTIVIDADES ----------------

    def register_actividad(self, id, nombre, fecha, ubicacion, capacidad_maxima):

        if self.act_repo.get(id):
            raise ValueError("Ya existe una actividad con ese ID")

        fecha_convertida = datetime.strptime(fecha, "%Y/%m/%d")

        if fecha_convertida.date() < datetime.now().date():
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

    # ---------------- PARTICIPACIONES ----------------

    def register_participacion(self, id, voluntario_id, actividad_id, horas):

        if self.part_repo.get(id):
            raise ValueError("Ya existe una participación con ese ID")

        voluntario = self.vol_repo.get(voluntario_id)

        if not voluntario:
            raise ValueError("El voluntario no existe")

        if voluntario.estado.lower() == "inactivo":
            raise ValueError("El voluntario está inactivo")

        actividad = self.act_repo.get(actividad_id)

        if not actividad:
            raise ValueError("La actividad no existe")

        if horas <= 0 or horas > 24:
            raise ValueError("Las horas deben ser entre 1 y 24")

        participantes_actuales = 0

        for p in self.part_repo.get_all():
            if p.actividad_id == actividad_id:
                participantes_actuales += 1

        if participantes_actuales >= actividad.capacidad_maxima:
            raise ValueError("La actividad alcanzó su capacidad máxima")

        participacion = ParticipacionORM(
            id=id,
            voluntario_id=voluntario_id,
            actividad_id=actividad_id,
            horas=horas
        )

        return self.part_repo.create(participacion)

    def get_participaciones(self):
        return self.part_repo.get_all()

    # ---------------- REPORTES ----------------

    def voluntario_mas_horas(self):

        acumulado = {}

        for p in self.part_repo.get_all():

            if p.voluntario_id not in acumulado:
                acumulado[p.voluntario_id] = 0

            acumulado[p.voluntario_id] += p.horas

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

            if p.actividad_id not in conteo:
                conteo[p.actividad_id] = 0

            conteo[p.actividad_id] += 1

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