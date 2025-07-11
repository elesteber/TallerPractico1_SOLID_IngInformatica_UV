from typing import Dict, Any, List
from datetime import datetime
from models.Alumno import Alumno
from interfaces.IEstudiante import IEstudiante
from interfaces.Capabilities.IHaceClases import IHaceClases
from interfaces.Capabilities.IInvestiga import IInvestiga

class Titulado(Alumno, IEstudiante, IHaceClases, IInvestiga):
    """Persona titulada que puede hacer clases e investigar.
    Principio OCP: Nueva funcionalidad sin modificar código existente."""
    
    def __init__(self, id: str, nombre: str, apellido: str, email: str, fecha_ingreso: datetime, titulo: str, especialidad: str):
        super().__init__(id, nombre, apellido, email, fecha_ingreso)
        self._titulo = titulo
        self._especialidad = especialidad
        self._experiencia_anos = 0
        self._publicaciones: List[Dict[str, str]] = []
        self._asignaturas_docencia: List[str] = []
        self._estudiantes_dirigidos: List[str] = []
    
    @property
    def titulo(self) -> str:
        return self._titulo
    
    @property
    def especialidad(self) -> str:
        return self._especialidad
    
    @property
    def experiencia_anos(self) -> int:
        return self._experiencia_anos
    
    def aumentar_experiencia(self, anos: int) -> None:
        """Aumenta los años de experiencia."""
        self._experiencia_anos += anos
    
    def agregar_asignatura_docencia(self, asignatura: str) -> bool:
        """Agrega una asignatura donde puede hacer docencia."""
        if asignatura not in self._asignaturas_docencia:
            self._asignaturas_docencia.append(asignatura)
            return True
        return False
    
    # Implementación de IEstudiante
    def obtener_info_basica(self) -> Dict[str, Any]:
        """Obtiene información básica del titulado."""
        return {
            'id': self._id,
            'nombre': self._nombre,
            'apellido': self._apellido,
            'tipo': self.obtener_tipo_estudiante(),
            'titulo': self._titulo,
            'especialidad': self._especialidad,
            'experiencia_anos': self._experiencia_anos,
            'asignaturas_docencia': len(self._asignaturas_docencia),
            'publicaciones': len(self._publicaciones)
        }
    
    def obtener_tipo_estudiante(self) -> str:
        """Retorna el tipo de estudiante."""
        return "Titulado/Profesor"
    
    # Implementación de IHaceClases
    def dictar_clase(self, asignatura: str, tema: str) -> str:
        """Método para dictar una clase como profesor."""
        if asignatura in self._asignaturas_docencia:
            return f"El profesor {self._nombre} ({self._titulo}) dictó una clase de {tema} en {asignatura}"
        return f"El profesor {self._nombre} no está asignado para dictar clases en {asignatura}"
    
    def evaluar_estudiantes(self, estudiantes: List[str]) -> dict:
        """Método para evaluar estudiantes como profesor."""
        resultados = {}
        for estudiante in estudiantes:
            resultados[estudiante] = f"Evaluado por {self._titulo} con {self._experiencia_anos} años de experiencia"
        return resultados
    
    def preparar_material(self, asignatura: str) -> List[str]:
        """Prepara el material de clase como profesor."""
        if asignatura in self._asignaturas_docencia:
            return [
                f"Material profesional para {asignatura}",
                f"Casos prácticos de {self._especialidad}",
                f"Experiencia profesional aplicada a {asignatura}",
                "Evaluaciones y rúbricas"
            ]
        return []
    
    # Implementación de IInvestiga
    def realizar_investigacion(self, tema: str) -> str:
        """Realiza una investigación sobre un tema específico."""
        return f"El {self._titulo} {self._nombre} está realizando investigación avanzada sobre: {tema}"
    
    def publicar_articulo(self, titulo: str, contenido: str) -> bool:
        """Publica un artículo de investigación."""
        articulo = {
            'titulo': titulo,
            'contenido': contenido,
            'autor': f"{self._titulo} {self._nombre} {self._apellido}",
            'especialidad': self._especialidad,
            'fecha': datetime.now().isoformat()
        }
        self._publicaciones.append(articulo)
        return True
    
    def obtener_publicaciones(self) -> List[Dict[str, str]]:
        """Obtiene la lista de publicaciones realizadas."""
        return self._publicaciones.copy()
    
    def dirigir_tesis(self, estudiante: str, tema: str) -> str:
        """Dirige una tesis de estudiante."""
        self._estudiantes_dirigidos.append(estudiante)
        return f"El {self._titulo} {self._nombre} está dirigiendo la tesis de {estudiante} sobre: {tema}"
    
    def __str__(self) -> str:
        return f"{self._titulo}: {self._nombre} {self._apellido} - {self._especialidad} ({self._experiencia_anos} años exp.)"