from fastapi import APIRouter, HTTPException

from app.service.voluntariado_service import VoluntariadoService
from app.schemas.voluntario_schema import VoluntarioSchema

router = APIRouter(prefix="/voluntarios", tags=["Voluntarios"])

service = VoluntariadoService()


@router.post("", response_model=VoluntarioSchema)
def create_voluntario(voluntario: VoluntarioSchema):

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
def list_voluntarios():
    return service.get_voluntarios()