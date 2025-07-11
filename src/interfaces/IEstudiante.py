from abc import ABC, abstractmethod
from typing import Dict, Any

class IEstudiante(ABC):
    """Interfaz base para todos los tipos de estudiantes.
    Principio ISP: Interfaz mínima común para estudiantes."""
    
    @abstractmethod
    def obtener_info_basica(self) -> Dict[str, Any]:
        """Obtiene información básica del estudiante."""
        pass
    
    @abstractmethod
    def obtener_tipo_estudiante(self) -> str:
        """Retorna el tipo de estudiante."""
        pass