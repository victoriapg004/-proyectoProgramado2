from fastapi import APIRouter, HTTPException

from app.service.voluntariado_service import VoluntariadoService
from app.schemas.participacion_schema import ParticipacionSchema
from app.config.dependencies import get_current_user
from fastapi import Depends

router = APIRouter(prefix="/participaciones", tags=["Participaciones"])

service = VoluntariadoService()


@router.post("", response_model=ParticipacionSchema)
def create_participacion(participacion: ParticipacionSchema,user=Depends(get_current_user)):

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
def list_participaciones(user=Depends(get_current_user)):
    return service.get_participaciones()

@router.put("", response_model=ParticipacionSchema)
def update_participacion(participacion: ParticipacionSchema, user=Depends(get_current_user)):

    try:

        resultado = service.update_participacion(
            participacion.id,
            participacion.voluntario_id,
            participacion.actividad_id,
            participacion.horas
        )

        if not resultado:
            raise HTTPException(status_code=404, detail="Participación no encontrada")

        return resultado

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{participacion_id}")
def delete_participacion(participacion_id: str, user=Depends(get_current_user)):

    resultado = service.delete_participacion(participacion_id)

    if not resultado:
        raise HTTPException(status_code=404, detail="Participación no encontrada")

    return {"mensaje": "Participación eliminada correctamente"}