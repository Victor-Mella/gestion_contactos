from fastapi import FastAPI
from src.app.interface.router.contacto_router import router as contacto_router

app = FastAPI(
    title="API- Gestion de contactos",
    description="Mi segunda api, con variedad de verificaciones en el numero telefonico",
    version="1.0.0"
)

app.include_router(contacto_router, prefix="/api")
