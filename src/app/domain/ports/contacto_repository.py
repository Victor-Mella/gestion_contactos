from abc import ABC, abstractclassmethod
from typing import List, Optional
from src.app.domain.entities.contacto import Contacto


class ContactoRepository(ABC):

    @abstractclassmethod
    def obtener_todos(self) -> List[Contacto]:
        pass

    @abstractclassmethod
    def obtener_por_id(self, id: int) -> Optional[Contacto]:
        pass

    @abstractclassmethod
    def buscar_por_numero(self, numero: str) -> Optional[Contacto]:
        pass

    @abstractclassmethod
    def actualizar(self, contacto: Contacto) -> Contacto:
        pass

    @abstractclassmethod
    def eliminar(self, id: int) -> None:
        pass
