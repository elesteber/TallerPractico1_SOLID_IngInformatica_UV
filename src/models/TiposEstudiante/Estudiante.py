from typing import Dict, Any, List
from datetime import datetime
from models.Alumno import Alumno
from interfaces.IEstudiante import IEstudiante
from interfaces.Capabilities.IEstudia import IEstudia

class Estudiante(Alumno, IEstudiante, IEstudia):
    """Estudiante regular de pregrado.
    Principio LSP: Puede sustituir a IEstudiante sin alterar el comportamiento."""
    
    def __init__(self, id: str, nombre: str, apellido: str, email: str, fecha_ingreso: datetime, carrera: str):
        super().__init__(id, nombre, apellido, email, fecha_ingreso)
        self._carrera = carrera
        self._semestre_actual = 1
    
    @property
    def carrera(self) -> str:
        return self._carrera
    
    @property
    def semestre_actual(self) -> int:
        return self._semestre_actual
    
    def avanzar_semestre(self) -> None:
        """Avanza al siguiente semestre."""
        self._semestre_actual += 1
    
    # Implementación de IEstudiante
    def obtener_info_basica(self) -> Dict[str, Any]:
        """Obtiene información básica del estudiante."""
        return {
            'id': self._id,
            'nombre': self._nombre,
            'apellido': self._apellido,
            'tipo': self.obtener_tipo_estudiante(),
            'carrera': self._carrera,
            'semestre': self._semestre_actual
        }
    
    def obtener_tipo_estudiante(self) -> str:
        """Retorna el tipo de estudiante."""
        return "Estudiante Pregrado"
    
    # Implementación de IEstudia
    def estudiar(self, materia: str) -> str:
        """Método para estudiar una materia específica."""
        return f"{self._nombre} está estudiando {materia} para su carrera de {self._carrera}"
    
    def presentar_examen(self, asignatura: str) -> bool:
        """Método para presentar un examen."""
        if asignatura in self._asignaturas_matriculadas:
            return True
        return False
    
    def obtener_materias_cursando(self) -> List[str]:
        """Obtiene las materias que está cursando actualmente."""
        return self._asignaturas_matriculadas.copy()
    
    def __str__(self) -> str:
        return f"Estudiante: {self._nombre} {self._apellido} - {self._carrera} (Semestre {self._semestre_actual})"