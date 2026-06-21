from fastapi import APIRouter, HTTPException

from app.service.voluntariado_service import VoluntariadoService
from app.schemas.participacion_schema import ParticipacionSchema

router = APIRouter(prefix="/participaciones", tags=["Participaciones"])

service = VoluntariadoService()


@router.post("", response_model=ParticipacionSchema)
def create_participacion(participacion: ParticipacionSchema):

    try:
        return service.register_participacion(
            participacion.id,
            participacion.voluntario_id,
            participacion.actividad_id,
            participacion.horas
        )

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("", response_model=list[ParticipacionSchema])
def list_participaciones():
    return service.get_participaciones()