from fastapi import APIRouter, HTTPException

from app.service.voluntariado_service import VoluntariadoService
from app.schemas.voluntario_schema import VoluntarioSchema
from app.config.dependencies import get_current_user
from fastapi import Depends

router = APIRouter(prefix="/voluntarios", tags=["Voluntarios"])

service = VoluntariadoService()


@router.post("", response_model=VoluntarioSchema)
def create_voluntario(voluntario: VoluntarioSchema,user=Depends(get_current_user)):

    try:
        return service.register_voluntario(
            voluntario.id,
            voluntario.nombre,
            voluntario.telefono,
            voluntario.tipo,
            voluntario.estado
        )

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("", response_model=list[VoluntarioSchema])
def list_voluntarios(user=Depends(get_current_user)):
    return service.get_voluntarios()

@router.put("", response_model=VoluntarioSchema)
def update_voluntario(voluntario: VoluntarioSchema, user=Depends(get_current_user)):

    try:
        resultado = service.update_voluntario(
            voluntario.id,
            voluntario.nombre,
            voluntario.telefono,
            voluntario.tipo,
            voluntario.estado
        )

        if not resultado:
            raise HTTPException(status_code=404, detail="Voluntario no encontrado")

        return resultado

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{voluntario_id}")
def delete_voluntario(voluntario_id: str, user=Depends(get_current_user)):

    resultado = service.delete_voluntario(voluntario_id)

    if not resultado:
        raise HTTPException(status_code=404, detail="Voluntario no encontrado")

    return {"mensaje": "Voluntario eliminado correctamente"}