from abc import ABC, abstractmethod
from typing import List

class IEstudia(ABC):
    """Interfaz que define la capacidad de estudiar.
    Principio ISP: Interfaz específica para una sola responsabilidad."""
    
    @abstractmethod
    def estudiar(self, materia: str) -> str:
        """Método para estudiar una materia específica."""
        pass
    
    @abstractmethod
    def presentar_examen(self, asignatura: str) -> bool:
        """Método para presentar un examen."""
        pass
    
    @abstractmethod
    def obtener_materias_cursando(self) -> List[str]:
        """Obtiene las materias que está cursando actualmente."""
        pass