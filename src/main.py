"""
Sistema de Gestión de Aula Virtual - Universidad de Valparaíso
Taller Práctico 1: Implementación de Principios SOLID

Este archivo demuestra la implementación de los 5 principios SOLID:
1. SRP - Single Responsibility Principle
2. OCP - Open/Closed Principle  
3. LSP - Liskov Substitution Principle
4. ISP - Interface Segregation Principle
5. DIP - Dependency Inversion Principle
"""

from datetime import datetime
from repositories.RepositorioAlumnos import RepositorioAlumnos
from repositories.RepositorioAsignaturas import RepositorioAsignaturas
from services.GestorAlumnos import GestorAlumnos
from services.GestorAsignaturas import GestorAsignaturas

def main():
    print("=== Sistema de Gestión de Aula Virtual UV ===")
    print("Demostración de Principios SOLID\n")
    
    # Inicializar repositorios (DIP - Dependency Inversion)
    repo_alumnos = RepositorioAlumnos()
    repo_asignaturas = RepositorioAsignaturas()
    
    # Inicializar gestores con inyección de dependencias (DIP)
    gestor_alumnos = GestorAlumnos(repo_alumnos, repo_asignaturas)
    gestor_asignaturas = GestorAsignaturas(repo_asignaturas, repo_alumnos)
    
    # === Demostración de los principios SOLID ===
    
    print("1. Creando asignaturas...")
    # SRP: Cada clase tiene una sola responsabilidad
    gestor_asignaturas.crear_asignatura("ING001", "Programación I", 6, 1, "PROF001")
    gestor_asignaturas.crear_asignatura("ING002", "Matemáticas I", 8, 1, "PROF002")
    gestor_asignaturas.crear_asignatura("ING003", "Física I", 6, 2, "PROF003")
    
    print("2. Creando diferentes tipos de estudiantes...")
    # OCP: Nuevos tipos de estudiantes sin modificar código existente
    # LSP: Todos los estudiantes pueden sustituir a IEstudiante
    gestor_alumnos.crear_estudiante_pregrado("EST001", "Juan", "Pérez", "juan.perez@uv.cl", "Ingeniería Informática")
    gestor_alumnos.crear_estudiante_ayudante("EST002", "María", "González", "maria.gonzalez@uv.cl", "Ingeniería Civil", ["ING001"])
    gestor_alumnos.crear_estudiante_magister("EST003", "Carlos", "Rodríguez", "carlos.rodriguez@uv.cl", "Magíster en Informática", "Machine Learning en Educación")
    gestor_alumnos.crear_estudiante_doctorado("EST004", "Ana", "López", "ana.lopez@uv.cl", "Doctorado en Informática", "IA en Sistemas Educativos", "Inteligencia Artificial")
    gestor_alumnos.crear_titulado("PROF001", "Dr. Pedro", "Martínez", "pedro.martinez@uv.cl", "Doctor en Ciencias", "Programación")
    
    print("3. Matriculando estudiantes en asignaturas...")
    gestor_alumnos.matricular_alumno("EST001", "ING001")
    gestor_alumnos.matricular_alumno("EST001", "ING002")
    gestor_alumnos.matricular_alumno("EST002", "ING002")
    gestor_alumnos.matricular_alumno("EST003", "ING003")
    
    print("\n=== Demostración de las capacidades específicas (ISP) ===")
    
    # ISP: Interfaces segregadas - cada estudiante implementa solo lo que necesita
    estudiante_pregrado = gestor_alumnos.obtener_alumno("EST001")
    estudiante_ayudante = gestor_alumnos.obtener_alumno("EST002")
    estudiante_magister = gestor_alumnos.obtener_alumno("EST003")
    estudiante_doctorado = gestor_alumnos.obtener_alumno("EST004")
    profesor = gestor_alumnos.obtener_alumno("PROF001")
    
    print("\n--- Capacidad de Estudiar (IEstudia) ---")
    if hasattr(estudiante_pregrado, 'estudiar'):
        print(f"- {estudiante_pregrado.estudiar('Programación')}")
    if hasattr(estudiante_ayudante, 'estudiar'):
        print(f"- {estudiante_ayudante.estudiar('Algoritmos')}")
    
    print("\n--- Capacidad de Hacer Clases (IHaceClases) ---")
    if hasattr(estudiante_ayudante, 'dictar_clase'):
        print(f"- {estudiante_ayudante.dictar_clase('ING001', 'Variables y Tipos de Datos')}")
    if hasattr(estudiante_doctorado, 'dictar_clase'):
        print(f"- {estudiante_doctorado.dictar_clase('ING003', 'Mecánica Cuántica')}")
    if hasattr(profesor, 'dictar_clase'):
        profesor.agregar_asignatura_docencia("ING001")
        print(f"- {profesor.dictar_clase('ING001', 'Introducción a la Programación')}")
    
    print("\n--- Capacidad de Investigar (IInvestiga) ---")
    if hasattr(estudiante_magister, 'realizar_investigacion'):
        print(f"- {estudiante_magister.realizar_investigacion('Algoritmos de Aprendizaje Automático')}")
        estudiante_magister.publicar_articulo("ML en Educación", "Artículo sobre machine learning aplicado a sistemas educativos")
    if hasattr(estudiante_doctorado, 'dirigir_tesis'):
        print(f"- {estudiante_doctorado.dirigir_tesis('EST005', 'Redes Neuronales en Educación')}")
    if hasattr(profesor, 'publicar_articulo'):
        profesor.publicar_articulo("Nuevos Paradigmas en Programación", "Artículo sobre tendencias en programación")
    
    print("\n=== Estadísticas del Sistema ===")
    
    # Mostrar estadísticas usando polimorfismo (LSP)
    print("\n--- Información de Estudiantes ---")
    alumnos = gestor_alumnos.listar_todos_alumnos()
    for alumno in alumnos:
        if hasattr(alumno, 'obtener_info_basica'):
            info = alumno.obtener_info_basica()
            print(f"- {info['nombre']} {info['apellido']} ({info['tipo']})")
    
    print("\n--- Estadísticas Generales ---")
    stats_alumnos = gestor_alumnos.obtener_estadisticas()
    print(f"Total de alumnos: {stats_alumnos['total_alumnos']}")
    print(f"Total de matrículas: {stats_alumnos['total_matriculas']}")
    print("Distribución por tipo:")
    for tipo, cantidad in stats_alumnos['tipos_estudiantes'].items():
        print(f"  - {tipo}: {cantidad}")
    
    stats_asignaturas = gestor_asignaturas.obtener_estadisticas_generales()
    print(f"\nTotal de asignaturas: {stats_asignaturas['total_asignaturas']}")
    print(f"Total de créditos: {stats_asignaturas['total_creditos']}")
    print(f"Promedio de créditos por asignatura: {stats_asignaturas['promedio_creditos_por_asignatura']:.1f}")
    
    print("\n--- Carga del Profesor ---")
    carga_prof = gestor_asignaturas.obtener_carga_profesor("PROF001")
    print(f"Profesor PROF001:")
    print(f"  - Asignaturas: {carga_prof['total_asignaturas']}")
    print(f"  - Créditos: {carga_prof['total_creditos']}")
    print(f"  - Estudiantes: {carga_prof['total_estudiantes']}")
    
    print("\n=== Resumen de Principios SOLID Implementados ===")
    print("✓ SRP: Cada clase tiene una sola responsabilidad")
    print("  - Alumno: maneja datos básicos")
    print("  - Asignatura: maneja datos de asignatura")
    print("  - Repositorios: manejan persistencia")
    print("  - Gestores: manejan lógica de negocio")
    
    print("\n✓ OCP: Extensible sin modificar código existente")
    print("  - Nuevos tipos de estudiantes heredan de clases base")
    print("  - Nuevas capacidades se agregan vía interfaces")
    
    print("\n✓ LSP: Los subtipos pueden sustituir a sus tipos base")
    print("  - Todos los estudiantes implementan IEstudiante")
    print("  - Pueden usarse polimórficamente")
    
    print("\n✓ ISP: Interfaces específicas y segregadas")
    print("  - IEstudia: solo para quienes estudian")
    print("  - IHaceClases: solo para quienes enseñan")
    print("  - IInvestiga: solo para quienes investigan")
    
    print("\n✓ DIP: Dependencias hacia abstracciones")
    print("  - Gestores dependen de IRepositorio, no implementaciones")
    print("  - Inyección de dependencias en constructores")

if __name__ == "__main__":
    main()