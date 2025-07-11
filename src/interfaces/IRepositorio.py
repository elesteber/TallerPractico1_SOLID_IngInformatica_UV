from abc import ABC, abstractmethod
from typing import List, Optional, Any

class IRepositorio(ABC):
    """Interfaz genérica para repositorios.
    Principio DIP: Abstracción para el acceso a datos."""
    
    @abstractmethod
    def agregar(self, item: Any) -> bool:
        """Agrega un elemento al repositorio."""
        pass
    
    @abstractmethod
    def obtener_por_id(self, id: str) -> Optional[Any]:
        """Obtiene un elemento por su ID."""
        pass
    
    @abstractmethod
    def obtener_todos(self) -> List[Any]:
        """Obtiene todos los elementos del repositorio."""
        pass
    
    @abstractmethod
    def actualizar(self, id: str, item: Any) -> bool:
        """Actualiza un elemento en el repositorio."""
        pass
    
    @abstractmethod
    def eliminar(self, id: str) -> bool:
        """Elimina un elemento del repositorio."""
        pass
    
    @abstractmethod
    def buscar(self, criterio: dict) -> List[Any]:
        """Busca elementos según un criterio específico."""
        pass