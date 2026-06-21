from fastapi import APIRouter, HTTPException

from app.service.voluntariado_service import VoluntariadoService
from app.schemas.actividad_schema import ActividadSchema

router = APIRouter(prefix="/actividades", tags=["Actividades"])

service = VoluntariadoService()


@router.post("", response_model=ActividadSchema)
def create_actividad(actividad: ActividadSchema):

    try:
        return service.register_actividad(
            actividad.id,
            actividad.nombre,
            actividad.fecha,
            actividad.ubicacion,
            actividad.capacidad_maxima
        )

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("", response_model=list[ActividadSchema])
def list_actividades():
    return service.get_actividades()