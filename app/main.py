from fastapi import FastAPI

from app.controller.voluntario_controller import router as voluntario_router
from app.controller.actividad_controller import router as actividad_router
from app.controller.participacion_controller import router as participacion_router
from app.controller.reporte_controller import router as reporte_router


app = FastAPI(
    title="Sistema de Voluntariado",
    version="1.0"
)


# ---------------- ROUTERS ----------------

app.include_router(voluntario_router)
app.include_router(actividad_router)
app.include_router(participacion_router)
app.include_router(reporte_router)


# ---------------- ROOT ----------------

@app.get("/")
def root():
    return {"message": "API de Voluntariado funcionando correctamente"}