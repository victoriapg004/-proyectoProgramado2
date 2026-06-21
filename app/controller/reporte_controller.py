from fastapi import APIRouter

from app.service.voluntariado_service import VoluntariadoService

router = APIRouter(prefix="/reportes", tags=["Reportes"])

service = VoluntariadoService()


# ---------------- REPORTE 1 ----------------
@router.get("/voluntario-mas-horas")
def voluntario_mas_horas():
    return service.voluntario_mas_horas()


# ---------------- REPORTE 2 ----------------
@router.get("/actividad-mas-participacion")
def actividad_mas_participacion():
    return service.actividad_mas_participacion()


# ---------------- REPORTE 3 ----------------
@router.get("/voluntarios-activos")
def voluntarios_activos():
    return service.cantidad_voluntarios_activos()