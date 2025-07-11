from typing import Dict, Any, List
from datetime import datetime

class Asignatura:
    """Clase que representa una asignatura en el sistema.
    Principio SRP: Se encarga únicamente de los datos de la asignatura."""
    
    def __init__(self, id: str, nombre: str, creditos: int, semestre: int, profesor_id: str):
        self._id = id
        self._nombre = nombre
        self._creditos = creditos
        self._semestre = semestre
        self._profesor_id = profesor_id
        self._estudiantes_matriculados: List[str] = []
        self._fecha_creacion = datetime.now()
    
    @property
    def id(self) -> str:
        return self._id
    
    @property
    def nombre(self) -> str:
        return self._nombre
    
    @property
    def creditos(self) -> int:
        return self._creditos
    
    @property
    def semestre(self) -> int:
        return self._semestre
    
    @property
    def profesor_id(self) -> str:
        return self._profesor_id
    
    @property
    def estudiantes_matriculados(self) -> List[str]:
        return self._estudiantes_matriculados.copy()
    
    @property
    def fecha_creacion(self) -> datetime:
        return self._fecha_creacion
    
    def agregar_estudiante(self, estudiante_id: str) -> bool:
        """Agrega un estudiante a la asignatura."""
        if estudiante_id not in self._estudiantes_matriculados:
            self._estudiantes_matriculados.append(estudiante_id)
            return True
        return False
    
    def remover_estudiante(self, estudiante_id: str) -> bool:
        """Remueve un estudiante de la asignatura."""
        if estudiante_id in self._estudiantes_matriculados:
            self._estudiantes_matriculados.remove(estudiante_id)
            return True
        return False
    
    def obtener_cantidad_estudiantes(self) -> int:
        """Obtiene la cantidad de estudiantes matriculados."""
        return len(self._estudiantes_matriculados)
    
    def obtener_info_completa(self) -> Dict[str, Any]:
        """Obtiene toda la información de la asignatura."""
        return {
            'id': self._id,
            'nombre': self._nombre,
            'creditos': self._creditos,
            'semestre': self._semestre,
            'profesor_id': self._profesor_id,
            'estudiantes_matriculados': self._estudiantes_matriculados.copy(),
            'cantidad_estudiantes': len(self._estudiantes_matriculados),
            'fecha_creacion': self._fecha_creacion.isoformat()
        }
    
    def __str__(self) -> str:
        return f"Asignatura: {self._nombre} ({self._id}) - {self._creditos} créditos"