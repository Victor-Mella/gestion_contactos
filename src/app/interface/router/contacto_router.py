from fastapi import APIRouter, Depends, HTTPException
from typing import List
from src.app.domain.entities.contacto import Contacto
from src.app.aplication.services.contacto_services import ContactoService
from src.app.infrastucture.repositories.contacto_repository_impl import ContactoRepositoryImpl

router = APIRouter()
contacto_service = ContactoService(ContactoRepositoryImpl)


@router.get("/contactos", response_model=List[Contacto])
def listar_contactos():
    return contacto_service.listar_contactos()


@router.get("/contactos/{id}", response_model=Contacto)
def obtener_contacto(id: int):
    contacto = contacto_service.obtener_contacto(id)
    if not contacto:
        raise HTTPException(
            status_code=404, detail="El contacto no se encontro")
    return contacto


@router.post("/contactos", response_model=Contacto)
def crear_contacto(contacto: Contacto):
    try:
        return contacto_service.crear_contacto(contacto)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/contactos/{id}", response_model=Contacto)
def actualizar_contacto(id: int, contacto: Contacto):
    contacto_existente = contacto_service.obtener_contacto(id)
    if not contacto_existente:
        raise HTTPException(
            status_code=404, detail="No se ha encontrado el contacto")
    contacto.id = id
    return contacto_service.actualizar_contacto(contacto)


@router.delete("/contactos/{id}")
def eliminar_contacto(id: int):
    contacto_existente = contacto_service.obtener_contacto(id)
    if not contacto_existente:
        raise HTTPException(
            status_code=404, detail="El contacto que se desea borrar no se encuentra")
    contacto_service.eliminar_contacto(id)
    return {"message: " "Contacto eliminado"}
