from abc import ABC, abstractmethod
from typing import List

class IHaceClases(ABC):
    """Interfaz que define la capacidad de dar clases.
    Principio ISP: Interfaz específica para profesores/ayudantes."""
    
    @abstractmethod
    def dictar_clase(self, asignatura: str, tema: str) -> str:
        """Método para dictar una clase."""
        pass
    
    @abstractmethod
    def evaluar_estudiantes(self, estudiantes: List[str]) -> dict:
        """Método para evaluar estudiantes."""
        pass
    
    @abstractmethod
    def preparar_material(self, asignatura: str) -> List[str]:
        """Prepara el material de clase."""
        pass