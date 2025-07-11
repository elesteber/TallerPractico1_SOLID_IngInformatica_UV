from typing import List, Optional, Any, Dict
from interfaces.IRepositorio import IRepositorio
from models.Asignatura import Asignatura

class RepositorioAsignaturas(IRepositorio):
    """Repositorio concreto para manejar asignaturas.
    Principio DIP: Implementa la abstracción IRepositorio."""
    
    def __init__(self):
        self._asignaturas: Dict[str, Asignatura] = {}
    
    def agregar(self, asignatura: Asignatura) -> bool:
        """Agrega una asignatura al repositorio."""
        if not isinstance(asignatura, Asignatura):
            return False
        
        if asignatura.id not in self._asignaturas:
            self._asignaturas[asignatura.id] = asignatura
            return True
        return False
    
    def obtener_por_id(self, id: str) -> Optional[Asignatura]:
        """Obtiene una asignatura por su ID."""
        return self._asignaturas.get(id)
    
    def obtener_todos(self) -> List[Asignatura]:
        """Obtiene todas las asignaturas del repositorio."""
        return list(self._asignaturas.values())
    
    def actualizar(self, id: str, asignatura: Asignatura) -> bool:
        """Actualiza una asignatura en el repositorio."""
        if id in self._asignaturas and isinstance(asignatura, Asignatura):
            self._asignaturas[id] = asignatura
            return True
        return False
    
    def eliminar(self, id: str) -> bool:
        """Elimina una asignatura del repositorio."""
        if id in self._asignaturas:
            del self._asignaturas[id]
            return True
        return False
    
    def buscar(self, criterio: dict) -> List[Asignatura]:
        """Busca asignaturas según un criterio específico."""
        resultado = []
        
        for asignatura in self._asignaturas.values():
            cumple_criterio = True
            
            if 'nombre' in criterio:
                if criterio['nombre'].lower() not in asignatura.nombre.lower():
                    cumple_criterio = False
            
            if 'creditos' in criterio:
                if asignatura.creditos != criterio['creditos']:
                    cumple_criterio = False
            
            if 'semestre' in criterio:
                if asignatura.semestre != criterio['semestre']:
                    cumple_criterio = False
            
            if 'profesor_id' in criterio:
                if asignatura.profesor_id != criterio['profesor_id']:
                    cumple_criterio = False
            
            if cumple_criterio:
                resultado.append(asignatura)
        
        return resultado
    
    def buscar_por_profesor(self, profesor_id: str) -> List[Asignatura]:
        """Busca asignaturas de un profesor específico."""
        resultado = []
        for asignatura in self._asignaturas.values():
            if asignatura.profesor_id == profesor_id:
                resultado.append(asignatura)
        return resultado
    
    def buscar_por_semestre(self, semestre: int) -> List[Asignatura]:
        """Busca asignaturas de un semestre específico."""
        resultado = []
        for asignatura in self._asignaturas.values():
            if asignatura.semestre == semestre:
                resultado.append(asignatura)
        return resultado
    
    def obtener_total_creditos_semestre(self, semestre: int) -> int:
        """Obtiene el total de créditos de un semestre."""
        total = 0
        for asignatura in self._asignaturas.values():
            if asignatura.semestre == semestre:
                total += asignatura.creditos
        return total
    
    def obtener_cantidad_total(self) -> int:
        """Obtiene la cantidad total de asignaturas."""
        return len(self._asignaturas)
    
    def existe_asignatura(self, id: str) -> bool:
        """Verifica si existe una asignatura con el ID dado."""
        return id in self._asignaturas