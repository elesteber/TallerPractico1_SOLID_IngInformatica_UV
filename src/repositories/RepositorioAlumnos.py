from typing import List, Optional, Any, Dict
from interfaces.IRepositorio import IRepositorio
from models.Alumno import Alumno

class RepositorioAlumnos(IRepositorio):
    """Repositorio concreto para manejar alumnos.
    Principio DIP: Implementa la abstracción IRepositorio."""
    
    def __init__(self):
        self._alumnos: Dict[str, Alumno] = {}
    
    def agregar(self, alumno: Alumno) -> bool:
        """Agrega un alumno al repositorio."""
        if not isinstance(alumno, Alumno):
            return False
        
        if alumno.id not in self._alumnos:
            self._alumnos[alumno.id] = alumno
            return True
        return False
    
    def obtener_por_id(self, id: str) -> Optional[Alumno]:
        """Obtiene un alumno por su ID."""
        return self._alumnos.get(id)
    
    def obtener_todos(self) -> List[Alumno]:
        """Obtiene todos los alumnos del repositorio."""
        return list(self._alumnos.values())
    
    def actualizar(self, id: str, alumno: Alumno) -> bool:
        """Actualiza un alumno en el repositorio."""
        if id in self._alumnos and isinstance(alumno, Alumno):
            self._alumnos[id] = alumno
            return True
        return False
    
    def eliminar(self, id: str) -> bool:
        """Elimina un alumno del repositorio."""
        if id in self._alumnos:
            del self._alumnos[id]
            return True
        return False
    
    def buscar(self, criterio: dict) -> List[Alumno]:
        """Busca alumnos según un criterio específico."""
        resultado = []
        
        for alumno in self._alumnos.values():
            cumple_criterio = True
            
            if 'nombre' in criterio:
                if criterio['nombre'].lower() not in alumno.nombre.lower():
                    cumple_criterio = False
            
            if 'apellido' in criterio:
                if criterio['apellido'].lower() not in alumno.apellido.lower():
                    cumple_criterio = False
            
            if 'email' in criterio:
                if criterio['email'].lower() not in alumno.email.lower():
                    cumple_criterio = False
            
            if cumple_criterio:
                resultado.append(alumno)
        
        return resultado
    
    def buscar_por_asignatura(self, asignatura_id: str) -> List[Alumno]:
        """Busca alumnos matriculados en una asignatura específica."""
        resultado = []
        for alumno in self._alumnos.values():
            if asignatura_id in alumno.asignaturas_matriculadas:
                resultado.append(alumno)
        return resultado
    
    def obtener_cantidad_total(self) -> int:
        """Obtiene la cantidad total de alumnos."""
        return len(self._alumnos)
    
    def existe_alumno(self, id: str) -> bool:
        """Verifica si existe un alumno con el ID dado."""
        return id in self._alumnos