from typing import List, Optional, Dict, Any
from datetime import datetime
from interfaces.IRepositorio import IRepositorio
from models.Alumno import Alumno
from models.TiposEstudiante.Estudiante import Estudiante
from models.TiposEstudiante.EstudianteAyudante import EstudianteAyudante
from models.TiposEstudiante.EstudianteMagister import EstudianteMagister
from models.TiposEstudiante.EstudianteDoctorado import EstudianteDoctorado
from models.TiposEstudiante.Titulado import Titulado

class GestorAlumnos:
    """Servicio para gestionar alumnos.
    Principio SRP: Se encarga únicamente de la lógica de negocio de alumnos.
    Principio DIP: Depende de abstracciones (IRepositorio), no de implementaciones concretas."""
    
    def __init__(self, repositorio_alumnos: IRepositorio, repositorio_asignaturas: IRepositorio):
        self._repositorio_alumnos = repositorio_alumnos
        self._repositorio_asignaturas = repositorio_asignaturas
    
    def crear_estudiante_pregrado(self, id: str, nombre: str, apellido: str, email: str, carrera: str) -> bool:
        """Crea un nuevo estudiante de pregrado."""
        if self._repositorio_alumnos.existe_alumno(id):
            return False
        
        estudiante = Estudiante(id, nombre, apellido, email, datetime.now(), carrera)
        return self._repositorio_alumnos.agregar(estudiante)
    
    def crear_estudiante_ayudante(self, id: str, nombre: str, apellido: str, email: str, carrera: str, asignaturas_ayudantia: List[str] = None) -> bool:
        """Crea un nuevo estudiante ayudante."""
        if self._repositorio_alumnos.existe_alumno(id):
            return False
        
        ayudante = EstudianteAyudante(id, nombre, apellido, email, datetime.now(), carrera, asignaturas_ayudantia)
        return self._repositorio_alumnos.agregar(ayudante)
    
    def crear_estudiante_magister(self, id: str, nombre: str, apellido: str, email: str, carrera: str, tema_tesis: str) -> bool:
        """Crea un nuevo estudiante de magíster."""
        if self._repositorio_alumnos.existe_alumno(id):
            return False
        
        magister = EstudianteMagister(id, nombre, apellido, email, datetime.now(), carrera, tema_tesis)
        return self._repositorio_alumnos.agregar(magister)
    
    def crear_estudiante_doctorado(self, id: str, nombre: str, apellido: str, email: str, carrera: str, tema_tesis: str, linea_investigacion: str) -> bool:
        """Crea un nuevo estudiante de doctorado."""
        if self._repositorio_alumnos.existe_alumno(id):
            return False
        
        doctorado = EstudianteDoctorado(id, nombre, apellido, email, datetime.now(), carrera, tema_tesis, linea_investigacion)
        return self._repositorio_alumnos.agregar(doctorado)
    
    def crear_titulado(self, id: str, nombre: str, apellido: str, email: str, titulo: str, especialidad: str) -> bool:
        """Crea un nuevo titulado/profesor."""
        if self._repositorio_alumnos.existe_alumno(id):
            return False
        
        titulado = Titulado(id, nombre, apellido, email, datetime.now(), titulo, especialidad)
        return self._repositorio_alumnos.agregar(titulado)
    
    def matricular_alumno(self, alumno_id: str, asignatura_id: str) -> bool:
        """Matricula un alumno en una asignatura."""
        alumno = self._repositorio_alumnos.obtener_por_id(alumno_id)
        asignatura = self._repositorio_asignaturas.obtener_por_id(asignatura_id)
        
        if not alumno or not asignatura:
            return False
        
        # Matricular en ambos lados
        exito_alumno = alumno.matricular_asignatura(asignatura_id)
        exito_asignatura = asignatura.agregar_estudiante(alumno_id)
        
        if exito_alumno and exito_asignatura:
            # Actualizar en los repositorios
            self._repositorio_alumnos.actualizar(alumno_id, alumno)
            self._repositorio_asignaturas.actualizar(asignatura_id, asignatura)
            return True
        
        return False
    
    def desmatricular_alumno(self, alumno_id: str, asignatura_id: str) -> bool:
        """Desmatricula un alumno de una asignatura."""
        alumno = self._repositorio_alumnos.obtener_por_id(alumno_id)
        asignatura = self._repositorio_asignaturas.obtener_por_id(asignatura_id)
        
        if not alumno or not asignatura:
            return False
        
        # Desmatricular en ambos lados
        exito_alumno = alumno.desmatricular_asignatura(asignatura_id)
        exito_asignatura = asignatura.remover_estudiante(alumno_id)
        
        if exito_alumno and exito_asignatura:
            # Actualizar en los repositorios
            self._repositorio_alumnos.actualizar(alumno_id, alumno)
            self._repositorio_asignaturas.actualizar(asignatura_id, asignatura)
            return True
        
        return False
    
    def obtener_alumno(self, id: str) -> Optional[Alumno]:
        """Obtiene un alumno por su ID."""
        return self._repositorio_alumnos.obtener_por_id(id)
    
    def listar_todos_alumnos(self) -> List[Alumno]:
        """Lista todos los alumnos."""
        return self._repositorio_alumnos.obtener_todos()
    
    def buscar_alumnos(self, criterio: dict) -> List[Alumno]:
        """Busca alumnos según criterios específicos."""
        return self._repositorio_alumnos.buscar(criterio)
    
    def obtener_estadisticas(self) -> Dict[str, Any]:
        """Obtiene estadísticas generales de alumnos."""
        alumnos = self._repositorio_alumnos.obtener_todos()
        
        stats = {
            'total_alumnos': len(alumnos),
            'tipos_estudiantes': {},
            'total_matriculas': 0
        }
        
        for alumno in alumnos:
            # Contar por tipo
            if hasattr(alumno, 'obtener_tipo_estudiante'):
                tipo = alumno.obtener_tipo_estudiante()
                stats['tipos_estudiantes'][tipo] = stats['tipos_estudiantes'].get(tipo, 0) + 1
            
            # Contar matrículas
            stats['total_matriculas'] += len(alumno.asignaturas_matriculadas)
        
        return stats
    
    def eliminar_alumno(self, id: str) -> bool:
        """Elimina un alumno del sistema."""
        return self._repositorio_alumnos.eliminar(id)