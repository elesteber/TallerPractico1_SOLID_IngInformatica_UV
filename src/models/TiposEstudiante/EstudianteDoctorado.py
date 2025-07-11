from typing import Dict, Any, List
from datetime import datetime
from models.TiposEstudiante.EstudianteMagister import EstudianteMagister
from interfaces.Capabilities.IHaceClases import IHaceClases

class EstudianteDoctorado(EstudianteMagister, IHaceClases):
    """Estudiante de doctorado que puede investigar y hacer clases.
    Principio OCP: Extensión de funcionalidades sin modificar clases base."""
    
    def __init__(self, id: str, nombre: str, apellido: str, email: str, fecha_ingreso: datetime, carrera: str, tema_tesis: str, linea_investigacion: str):
        super().__init__(id, nombre, apellido, email, fecha_ingreso, carrera, tema_tesis)
        self._linea_investigacion = linea_investigacion
        self._estudiantes_dirigidos: List[str] = []
        self._asignaturas_docencia: List[str] = []
    
    @property
    def linea_investigacion(self) -> str:
        return self._linea_investigacion
    
    @property
    def estudiantes_dirigidos(self) -> List[str]:
        return self._estudiantes_dirigidos.copy()
    
    @property
    def asignaturas_docencia(self) -> List[str]:
        return self._asignaturas_docencia.copy()
    
    def agregar_asignatura_docencia(self, asignatura: str) -> bool:
        """Agrega una asignatura donde puede hacer docencia."""
        if asignatura not in self._asignaturas_docencia:
            self._asignaturas_docencia.append(asignatura)
            return True
        return False
    
    # Override del tipo de estudiante
    def obtener_tipo_estudiante(self) -> str:
        """Retorna el tipo de estudiante."""
        return "Estudiante Doctorado"
    
    def obtener_info_basica(self) -> Dict[str, Any]:
        """Obtiene información básica del estudiante de doctorado."""
        info = super().obtener_info_basica()
        info.update({
            'linea_investigacion': self._linea_investigacion,
            'estudiantes_dirigidos': len(self._estudiantes_dirigidos),
            'asignaturas_docencia': self._asignaturas_docencia.copy()
        })
        return info
    
    # Override de IInvestiga para doctorado
    def dirigir_tesis(self, estudiante: str, tema: str) -> str:
        """Dirige una tesis de estudiante (los doctorantes sí pueden)."""
        self._estudiantes_dirigidos.append(estudiante)
        return f"El doctorando {self._nombre} está dirigiendo la tesis de {estudiante} sobre: {tema}"
    
    # Implementación de IHaceClases
    def dictar_clase(self, asignatura: str, tema: str) -> str:
        """Método para dictar una clase como doctorando."""
        if asignatura in self._asignaturas_docencia:
            return f"El doctorando {self._nombre} dictó una clase de {tema} en {asignatura}"
        return f"El doctorando {self._nombre} no está autorizado para dictar clases en {asignatura}"
    
    def evaluar_estudiantes(self, estudiantes: List[str]) -> dict:
        """Método para evaluar estudiantes como doctorando."""
        resultados = {}
        for estudiante in estudiantes:
            resultados[estudiante] = "Evaluado por doctorando - Nivel avanzado"
        return resultados
    
    def preparar_material(self, asignatura: str) -> List[str]:
        """Prepara el material de clase como doctorando."""
        if asignatura in self._asignaturas_docencia:
            return [
                f"Material avanzado para {asignatura}",
                f"Investigación actual en {asignatura}",
                f"Papers relacionados con {self._linea_investigacion}"
            ]
        return []
    
    def __str__(self) -> str:
        return f"Estudiante Doctorado: {self._nombre} {self._apellido} - {self._linea_investigacion}"