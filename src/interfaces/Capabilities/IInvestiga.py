from abc import ABC, abstractmethod
from typing import List, Dict

class IInvestiga(ABC):
    """Interfaz que define la capacidad de investigar.
    Principio ISP: Interfaz específica para investigadores."""
    
    @abstractmethod
    def realizar_investigacion(self, tema: str) -> str:
        """Realiza una investigación sobre un tema específico."""
        pass
    
    @abstractmethod
    def publicar_articulo(self, titulo: str, contenido: str) -> bool:
        """Publica un artículo de investigación."""
        pass
    
    @abstractmethod
    def obtener_publicaciones(self) -> List[Dict[str, str]]:
        """Obtiene la lista de publicaciones realizadas."""
        pass
    
    @abstractmethod
    def dirigir_tesis(self, estudiante: str, tema: str) -> str:
        """Dirige una tesis de estudiante."""
        pass