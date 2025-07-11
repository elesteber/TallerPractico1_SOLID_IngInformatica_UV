from typing import List, Optional, Dict, Any
from interfaces.IRepositorio import IRepositorio
from models.Asignatura import Asignatura

class GestorAsignaturas:
    """Servicio para gestionar asignaturas.
    Principio SRP: Se encarga únicamente de la lógica de negocio de asignaturas.
    Principio DIP: Depende de abstracciones (IRepositorio), no de implementaciones concretas."""
    
    def __init__(self, repositorio_asignaturas: IRepositorio, repositorio_alumnos: IRepositorio):
        self._repositorio_asignaturas = repositorio_asignaturas
        self._repositorio_alumnos = repositorio_alumnos
    
    def crear_asignatura(self, id: str, nombre: str, creditos: int, semestre: int, profesor_id: str) -> bool:
        """Crea una nueva asignatura."""
        if self._repositorio_asignaturas.existe_asignatura(id):
            return False
        
        # Validaciones de negocio
        if creditos <= 0 or creditos > 12:
            return False
        
        if semestre < 1 or semestre > 10:
            return False
        
        asignatura = Asignatura(id, nombre, creditos, semestre, profesor_id)
        return self._repositorio_asignaturas.agregar(asignatura)
    
    def obtener_asignatura(self, id: str) -> Optional[Asignatura]:
        """Obtiene una asignatura por su ID."""
        return self._repositorio_asignaturas.obtener_por_id(id)
    
    def listar_todas_asignaturas(self) -> List[Asignatura]:
        """Lista todas las asignaturas."""
        return self._repositorio_asignaturas.obtener_todos()
    
    def listar_asignaturas_por_semestre(self, semestre: int) -> List[Asignatura]:
        """Lista asignaturas de un semestre específico."""
        return self._repositorio_asignaturas.buscar_por_semestre(semestre)
    
    def listar_asignaturas_por_profesor(self, profesor_id: str) -> List[Asignatura]:
        """Lista asignaturas de un profesor específico."""
        return self._repositorio_asignaturas.buscar_por_profesor(profesor_id)
    
    def buscar_asignaturas(self, criterio: dict) -> List[Asignatura]:
        """Busca asignaturas según criterios específicos."""
        return self._repositorio_asignaturas.buscar(criterio)
    
    def actualizar_asignatura(self, id: str, nombre: str = None, creditos: int = None, semestre: int = None, profesor_id: str = None) -> bool:
        """Actualiza los datos de una asignatura."""
        asignatura = self._repositorio_asignaturas.obtener_por_id(id)
        if not asignatura:
            return False
        
        # Crear nueva instancia con datos actualizados
        nueva_asignatura = Asignatura(
            id,
            nombre if nombre is not None else asignatura.nombre,
            creditos if creditos is not None else asignatura.creditos,
            semestre if semestre is not None else asignatura.semestre,
            profesor_id if profesor_id is not None else asignatura.profesor_id
        )
        
        # Mantener los estudiantes matriculados
        for estudiante_id in asignatura.estudiantes_matriculados:
            nueva_asignatura.agregar_estudiante(estudiante_id)
        
        return self._repositorio_asignaturas.actualizar(id, nueva_asignatura)
    
    def obtener_estudiantes_asignatura(self, asignatura_id: str) -> List[str]:
        """Obtiene la lista de estudiantes matriculados en una asignatura."""
        asignatura = self._repositorio_asignaturas.obtener_por_id(asignatura_id)
        if asignatura:
            return asignatura.estudiantes_matriculados
        return []
    
    def obtener_carga_profesor(self, profesor_id: str) -> Dict[str, Any]:
        """Obtiene la carga académica de un profesor."""
        asignaturas = self._repositorio_asignaturas.buscar_por_profesor(profesor_id)
        
        total_creditos = sum(asig.creditos for asig in asignaturas)
        total_estudiantes = sum(asig.obtener_cantidad_estudiantes() for asig in asignaturas)
        
        return {
            'profesor_id': profesor_id,
            'total_asignaturas': len(asignaturas),
            'total_creditos': total_creditos,
            'total_estudiantes': total_estudiantes,
            'asignaturas': [asig.obtener_info_completa() for asig in asignaturas]
        }
    
    def obtener_estadisticas_semestre(self, semestre: int) -> Dict[str, Any]:
        """Obtiene estadísticas de un semestre específico."""
        asignaturas = self._repositorio_asignaturas.buscar_por_semestre(semestre)
        
        total_creditos = sum(asig.creditos for asig in asignaturas)
        total_estudiantes = sum(asig.obtener_cantidad_estudiantes() for asig in asignaturas)
        
        # Agrupar por rango de créditos
        creditos_distribucion = {}
        for asig in asignaturas:
            creditos = asig.creditos
            creditos_distribucion[creditos] = creditos_distribucion.get(creditos, 0) + 1
        
        return {
            'semestre': semestre,
            'total_asignaturas': len(asignaturas),
            'total_creditos': total_creditos,
            'promedio_creditos': total_creditos / len(asignaturas) if asignaturas else 0,
            'total_estudiantes_matriculados': total_estudiantes,
            'distribucion_creditos': creditos_distribucion,
            'asignaturas': [asig.nombre for asig in asignaturas]
        }
    
    def obtener_estadisticas_generales(self) -> Dict[str, Any]:
        """Obtiene estadísticas generales del sistema de asignaturas."""
        asignaturas = self._repositorio_asignaturas.obtener_todos()
        
        if not asignaturas:
            return {'total_asignaturas': 0}
        
        total_creditos = sum(asig.creditos for asig in asignaturas)
        total_estudiantes = sum(asig.obtener_cantidad_estudiantes() for asig in asignaturas)
        
        # Estadísticas por semestre
        semestres = {}
        for asig in asignaturas:
            sem = asig.semestre
            if sem not in semestres:
                semestres[sem] = {'asignaturas': 0, 'creditos': 0, 'estudiantes': 0}
            semestres[sem]['asignaturas'] += 1
            semestres[sem]['creditos'] += asig.creditos
            semestres[sem]['estudiantes'] += asig.obtener_cantidad_estudiantes()
        
        return {
            'total_asignaturas': len(asignaturas),
            'total_creditos': total_creditos,
            'promedio_creditos_por_asignatura': total_creditos / len(asignaturas),
            'total_estudiantes_matriculados': total_estudiantes,
            'promedio_estudiantes_por_asignatura': total_estudiantes / len(asignaturas) if asignaturas else 0,
            'estadisticas_por_semestre': semestres
        }
    
    def eliminar_asignatura(self, id: str) -> bool:
        """Elimina una asignatura del sistema."""
        # Verificar si hay estudiantes matriculados
        asignatura = self._repositorio_asignaturas.obtener_por_id(id)
        if asignatura and len(asignatura.estudiantes_matriculados) > 0:
            return False  # No se puede eliminar si hay estudiantes matriculados
        
        return self._repositorio_asignaturas.eliminar(id)