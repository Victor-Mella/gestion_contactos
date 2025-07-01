from typing import List, Optional

from src.app.domain.entities.contacto import Contacto
from src.app.domain.ports.contacto_repository import ContactoRepository


class ContactoService:
    def __init__(self, contacto_repository: ContactoRepository):
        self._contacto_repository = contacto_repository

    def listar_contactos(self) -> List[Contacto]:
        return self._contacto_repository.obtener_todos()

    def obtener_contacto(self, id: int) -> Optional[Contacto]:
        return self._contacto_repository.obtener_por_id(id)

    def crear_contacto(self, contacto: Contacto) -> Contacto:
        numero = contacto.numero
        if not numero.startswith("+"):
            raise ValueError("El numero debe comenzar con '+'")
        if not numero[1:].isdigit():
            raise ValueError(
                "El numero solo debe tener digitos despues del '+'")
        if not (10 <= len(numero) <= 15):
            raise ValueError("El numero debe tener entre 10 y 15 caracteres")

        existente = self._contacto_repository.buscar_por_numero(numero)
        if existente:
            raise ValueError("Ya existe un contacto con ese numero")
        return self._contacto_repository.crear(contacto)

    def actualizar_contacto(self, contacto: Contacto) -> Contacto:
        return self._contacto_repository.actualizar(contacto)

    def eliminar_contacto(self, id: int) -> None:
        self._contacto_repository.eliminar(id)
