from fastapi import APIRouter, HTTPException

from app.service.voluntariado_service import VoluntariadoService
from app.schemas.actividad_schema import ActividadSchema
from app.config.dependencies import get_current_user
from fastapi import Depends

router = APIRouter(prefix="/actividades", tags=["Actividades"])

service = VoluntariadoService()


@router.post("", response_model=ActividadSchema)
def create_actividad(actividad: ActividadSchema,user=Depends(get_current_user)):

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
def list_actividades(user=Depends(get_current_user)):
    return service.get_actividades()

@router.put("", response_model=ActividadSchema)
def update_actividad(actividad: ActividadSchema, user=Depends(get_current_user)):

    try:

        resultado = service.update_actividad(
            actividad.id,
            actividad.nombre,
            actividad.fecha,
            actividad.ubicacion,
            actividad.capacidad_maxima
        )

        if not resultado:
            raise HTTPException(status_code=404, detail="Actividad no encontrada")

        return resultado

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{actividad_id}")
def delete_actividad(actividad_id: str, user=Depends(get_current_user)):

    resultado = service.delete_actividad(actividad_id)

    if not resultado:
        raise HTTPException(status_code=404, detail="Actividad no encontrada")

    return {"mensaje": "Actividad eliminada correctamente"}