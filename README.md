# Taller Práctico 1: Principios SOLID
## Sistema de Gestión de Aula Virtual - Universidad de Valparaíso

Solución completa para el Taller Práctico 1 de Metodología de Diseño, centrado en la implementación de los cinco principios S.O.L.I.D. en un sistema de gestión del Aula Virtual de la Universidad de Valparaíso (UV).

## 📋 Descripción del Proyecto

Este proyecto implementa un sistema de gestión académica que demuestra la aplicación práctica de los principios SOLID:

- **S**ingle Responsibility Principle (SRP)
- **O**pen/Closed Principle (OCP)
- **L**iskov Substitution Principle (LSP)
- **I**nterface Segregation Principle (ISP)
- **D**ependency Inversion Principle (DIP)

## 🏗️ Arquitectura del Sistema

```
src/
├── main.py                     # Punto de entrada del sistema
├── interfaces/                 # Interfaces y contratos (ISP, DIP)
│   ├── IEstudiante.py         # Interfaz base para estudiantes
│   ├── IRepositorio.py        # Interfaz para repositorios
│   └── Capabilities/          # Capacidades específicas (ISP)
│       ├── IEstudia.py        # Capacidad de estudiar
│       ├── IHaceClases.py     # Capacidad de enseñar
│       └── IInvestiga.py      # Capacidad de investigar
├── models/                    # Modelos de dominio (SRP)
│   ├── Alumno.py             # Clase base para alumnos
│   ├── Asignatura.py         # Clase para asignaturas
│   └── TiposEstudiante/      # Tipos específicos (OCP, LSP)
│       ├── Estudiante.py     # Estudiante de pregrado
│       ├── EstudianteAyudante.py
│       ├── EstudianteMagister.py
│       ├── EstudianteDoctorado.py
│       └── Titulado.py       # Profesores/Titulados
├── repositories/             # Capa de persistencia (DIP)
│   ├── RepositorioAlumnos.py
│   └── RepositorioAsignaturas.py
└── services/                 # Lógica de negocio (SRP, DIP)
    ├── GestorAlumnos.py
    └── GestorAsignaturas.py
```

## 🎯 Implementación de Principios SOLID

### 1. Single Responsibility Principle (SRP)
Cada clase tiene una única responsabilidad:
- `Alumno`: Maneja datos básicos del alumno
- `Asignatura`: Maneja datos de la asignatura
- `RepositorioAlumnos`: Maneja persistencia de alumnos
- `GestorAlumnos`: Maneja lógica de negocio de alumnos

### 2. Open/Closed Principle (OCP)
El sistema es extensible sin modificar código existente:
- Nuevos tipos de estudiantes heredan de clases base
- Nuevas capacidades se agregan mediante interfaces
- Ejemplo: `EstudianteDoctorado` extiende `EstudianteMagister`

### 3. Liskov Substitution Principle (LSP)
Los subtipos pueden sustituir a sus tipos base:
- Todos los estudiantes implementan `IEstudiante`
- Pueden ser usados polimórficamente
- Mantienen el comportamiento esperado

### 4. Interface Segregation Principle (ISP)
Interfaces específicas y segregadas:
- `IEstudia`: Solo para quienes estudian
- `IHaceClases`: Solo para quienes enseñan
- `IInvestiga`: Solo para quienes investigan
- Los clientes no dependen de interfaces que no usan

### 5. Dependency Inversion Principle (DIP)
Dependencias hacia abstracciones, no concreciones:
- `GestorAlumnos` depende de `IRepositorio`, no de implementaciones específicas
- Inyección de dependencias en constructores
- Facilita testing y mantenimiento

## 🚀 Cómo Ejecutar

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/tu-usuario/TallerPractico1_SOLID_IngInformatica_UV.git
   cd TallerPractico1_SOLID_IngInformatica_UV
   ```

2. **Ejecutar el sistema:**
   ```bash
   cd src
   python main.py
   ```

## 📊 Funcionalidades Implementadas

### Gestión de Estudiantes
- ✅ Crear estudiantes de pregrado
- ✅ Crear estudiantes ayudantes
- ✅ Crear estudiantes de magíster
- ✅ Crear estudiantes de doctorado
- ✅ Crear profesores/titulados
- ✅ Matricular/desmatricular en asignaturas
- ✅ Buscar estudiantes por criterios

### Gestión de Asignaturas
- ✅ Crear asignaturas
- ✅ Asignar profesores
- ✅ Gestionar matrículas
- ✅ Estadísticas por semestre
- ✅ Carga académica de profesores

### Capacidades Diferenciadas
- ✅ **Estudiar**: Estudiantes de pregrado, magíster, doctorado
- ✅ **Enseñar**: Ayudantes, doctorando, profesores
- ✅ **Investigar**: Estudiantes de magíster, doctorado, profesores

## 🧪 Ejemplo de Uso

```python
from repositories.RepositorioAlumnos import RepositorioAlumnos
from services.GestorAlumnos import GestorAlumnos

# Inicializar repositorios (DIP)
repo_alumnos = RepositorioAlumnos()
gestor = GestorAlumnos(repo_alumnos, repo_asignaturas)

# Crear diferentes tipos de estudiantes (OCP, LSP)
gestor.crear_estudiante_pregrado("EST001", "Juan", "Pérez", "juan@uv.cl", "Informática")
gestor.crear_estudiante_magister("EST002", "María", "González", "maria@uv.cl", "Informática", "IA en Educación")

# Usar polimórficamente (LSP)
estudiantes = gestor.listar_todos_alumnos()
for estudiante in estudiantes:
    print(estudiante.obtener_info_basica())  # Mismo método, diferentes implementaciones
```

## 📝 Casos de Uso Demostrados

1. **Matrícula de Estudiantes**: Un estudiante se matricula en múltiples asignaturas
2. **Ayudantías**: Un estudiante ayudante puede enseñar en asignaturas específicas
3. **Investigación**: Estudiantes de magíster y doctorado pueden publicar artículos
4. **Docencia**: Profesores y doctorando pueden dictar clases
5. **Estadísticas**: Generación de reportes del sistema

## 🎓 Valor Educativo

Este proyecto demuestra:
- **Diseño orientado a objetos** aplicando principios SOLID
- **Separación de responsabilidades** en capas bien definidas
- **Extensibilidad** sin modificar código existente
- **Polimorfismo** y sustitución de tipos
- **Inyección de dependencias** para bajo acoplamiento
- **Interfaces segregadas** para alta cohesión

## 📚 Conceptos Aplicados

- Herencia y Polimorfismo
- Composición sobre Herencia
- Patrón Repository
- Inyección de Dependencias
- Interface Segregation
- Abstracción y Encapsulación

## 🤝 Contribuciones

Este es un proyecto académico para demostrar principios SOLID. Las mejoras son bienvenidas siguiendo los mismos principios de diseño.

## 📄 Licencia

Proyecto académico - Universidad de Valparaíso

---
**Desarrollado para**: Taller Práctico 1 - Metodología de Diseño  
**Universidad**: Universidad de Valparaíso  
**Carrera**: Ingeniería en Informática
