from typing import Dict, Any, List
from datetime import datetime
from models.TiposEstudiante.Estudiante import Estudiante
from interfaces.Capabilities.IInvestiga import IInvestiga

class EstudianteMagister(Estudiante, IInvestiga):
    """Estudiante de magíster que puede investigar.
    Principio OCP: Extensible sin modificar la clase base."""
    
    def __init__(self, id: str, nombre: str, apellido: str, email: str, fecha_ingreso: datetime, carrera: str, tema_tesis: str):
        super().__init__(id, nombre, apellido, email, fecha_ingreso, carrera)
        self._tema_tesis = tema_tesis
        self._publicaciones: List[Dict[str, str]] = []
        self._director_tesis = ""
    
    @property
    def tema_tesis(self) -> str:
        return self._tema_tesis
    
    @property
    def director_tesis(self) -> str:
        return self._director_tesis
    
    def asignar_director_tesis(self, director: str) -> None:
        """Asigna un director de tesis."""
        self._director_tesis = director
    
    # Override del tipo de estudiante
    def obtener_tipo_estudiante(self) -> str:
        """Retorna el tipo de estudiante."""
        return "Estudiante Magíster"
    
    def obtener_info_basica(self) -> Dict[str, Any]:
        """Obtiene información básica del estudiante de magíster."""
        info = super().obtener_info_basica()
        info.update({
            'tema_tesis': self._tema_tesis,
            'director_tesis': self._director_tesis,
            'publicaciones': len(self._publicaciones)
        })
        return info
    
    # Implementación de IInvestiga
    def realizar_investigacion(self, tema: str) -> str:
        """Realiza una investigación sobre un tema específico."""
        return f"El estudiante de magíster {self._nombre} está investigando sobre: {tema}"
    
    def publicar_articulo(self, titulo: str, contenido: str) -> bool:
        """Publica un artículo de investigación."""
        articulo = {
            'titulo': titulo,
            'contenido': contenido,
            'autor': f"{self._nombre} {self._apellido}",
            'fecha': datetime.now().isoformat()
        }
        self._publicaciones.append(articulo)
        return True
    
    def obtener_publicaciones(self) -> List[Dict[str, str]]:
        """Obtiene la lista de publicaciones realizadas."""
        return self._publicaciones.copy()
    
    def dirigir_tesis(self, estudiante: str, tema: str) -> str:
        """Los estudiantes de magíster no pueden dirigir tesis."""
        return f"Los estudiantes de magíster no están autorizados para dirigir tesis"
    
    def __str__(self) -> str:
        return f"Estudiante Magíster: {self._nombre} {self._apellido} - Tesis: {self._tema_tesis}"