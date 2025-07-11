from typing import Dict, Any, List
from datetime import datetime
from models.TiposEstudiante.Estudiante import Estudiante
from interfaces.Capabilities.IHaceClases import IHaceClases

class EstudianteAyudante(Estudiante, IHaceClases):
    """Estudiante que además puede hacer clases como ayudante.
    Principio ISP: Implementa solo las interfaces que necesita."""
    
    def __init__(self, id: str, nombre: str, apellido: str, email: str, fecha_ingreso: datetime, carrera: str, asignaturas_ayudantia: List[str] = None):
        super().__init__(id, nombre, apellido, email, fecha_ingreso, carrera)
        self._asignaturas_ayudantia = asignaturas_ayudantia or []
        self._horas_ayudantia = 0
    
    @property
    def asignaturas_ayudantia(self) -> List[str]:
        return self._asignaturas_ayudantia.copy()
    
    @property
    def horas_ayudantia(self) -> int:
        return self._horas_ayudantia
    
    def agregar_asignatura_ayudantia(self, asignatura: str) -> bool:
        """Agrega una asignatura donde hace ayudantía."""
        if asignatura not in self._asignaturas_ayudantia:
            self._asignaturas_ayudantia.append(asignatura)
            return True
        return False
    
    # Override del tipo de estudiante
    def obtener_tipo_estudiante(self) -> str:
        """Retorna el tipo de estudiante."""
        return "Estudiante Ayudante"
    
    def obtener_info_basica(self) -> Dict[str, Any]:
        """Obtiene información básica del estudiante ayudante."""
        info = super().obtener_info_basica()
        info.update({
            'asignaturas_ayudantia': self._asignaturas_ayudantia.copy(),
            'horas_ayudantia': self._horas_ayudantia
        })
        return info
    
    # Implementación de IHaceClases
    def dictar_clase(self, asignatura: str, tema: str) -> str:
        """Método para dictar una clase como ayudante."""
        if asignatura in self._asignaturas_ayudantia:
            self._horas_ayudantia += 2
            return f"El ayudante {self._nombre} dictó una clase de {tema} en {asignatura}"
        return f"El ayudante {self._nombre} no está autorizado para dictar clases en {asignatura}"
    
    def evaluar_estudiantes(self, estudiantes: List[str]) -> dict:
        """Método para evaluar estudiantes como ayudante."""
        resultados = {}
        for estudiante in estudiantes:
            # Simulación de evaluación
            resultados[estudiante] = "Evaluado por ayudante"
        return resultados
    
    def preparar_material(self, asignatura: str) -> List[str]:
        """Prepara el material de clase como ayudante."""
        if asignatura in self._asignaturas_ayudantia:
            return [f"Material de apoyo para {asignatura}", f"Ejercicios prácticos de {asignatura}"]
        return []
    
    def __str__(self) -> str:
        return f"Estudiante Ayudante: {self._nombre} {self._apellido} - {self._carrera} (Ayudantías: {len(self._asignaturas_ayudantia)})"