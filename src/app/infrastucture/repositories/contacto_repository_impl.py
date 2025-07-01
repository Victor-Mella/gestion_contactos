from typing import List, Optional
from src.app.domain.entities.contacto import Contacto
from src.app.domain.ports.contacto_repository import ContactoRepository


class ContactoRepositoryImpl(ContactoRepository):
    def __init__(self):
        self._contactos = []
        self.id_counter = 1

    def obtener_todos(self) -> List[Contacto]:
        return self._contactos

    def obtener_por_id(self, id: int) -> Optional[Contacto]:
        for contacto in self._contactos:
            if contacto.id == id:
                return contacto
        return None

    def buscar_por_numero(self, numero: str) -> Optional[Contacto]:
        for contacto in self._contactos:
            if contacto.numero == numero:
                return contacto
        return None

    def crear(self, contacto: Contacto) -> Contacto:
        contacto.id = self.id_counter
        self.id_counter += 1
        self._contactos.append(contacto)
        return contacto

    def actualizar(self, contacto: Contacto) -> Contacto:
        for i, t in enumerate(self._contactos):
            if t.id == contacto.id:
                self._contactos[i] = contacto
                return contacto

    def eliminar(self, id: int) -> None:
        self._contactos = [t for t in self._contactos if t.id != id]
