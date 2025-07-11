from typing import Dict, Any, List
from datetime import datetime

class Alumno:
    """Clase que representa un alumno en el sistema.
    Principio SRP: Se encarga únicamente de manejar los datos básicos del alumno."""
    
    def __init__(self, id: str, nombre: str, apellido: str, email: str, fecha_ingreso: datetime):
        self._id = id
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._fecha_ingreso = fecha_ingreso
        self._asignaturas_matriculadas: List[str] = []
    
    @property
    def id(self) -> str:
        return self._id
    
    @property
    def nombre(self) -> str:
        return self._nombre
    
    @property
    def apellido(self) -> str:
        return self._apellido
    
    @property
    def email(self) -> str:
        return self._email
    
    @property
    def fecha_ingreso(self) -> datetime:
        return self._fecha_ingreso
    
    @property
    def asignaturas_matriculadas(self) -> List[str]:
        return self._asignaturas_matriculadas.copy()
    
    def matricular_asignatura(self, asignatura_id: str) -> bool:
        """Matricula al alumno en una asignatura."""
        if asignatura_id not in self._asignaturas_matriculadas:
            self._asignaturas_matriculadas.append(asignatura_id)
            return True
        return False
    
    def desmatricular_asignatura(self, asignatura_id: str) -> bool:
        """Desmatricula al alumno de una asignatura."""
        if asignatura_id in self._asignaturas_matriculadas:
            self._asignaturas_matriculadas.remove(asignatura_id)
            return True
        return False
    
    def obtener_info_completa(self) -> Dict[str, Any]:
        """Obtiene toda la información del alumno."""
        return {
            'id': self._id,
            'nombre': self._nombre,
            'apellido': self._apellido,
            'email': self._email,
            'fecha_ingreso': self._fecha_ingreso.isoformat(),
            'asignaturas_matriculadas': self._asignaturas_matriculadas.copy()
        }
    
    def __str__(self) -> str:
        return f"Alumno: {self._nombre} {self._apellido} ({self._id})"