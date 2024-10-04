# Django Project & Task Management App

Este proyecto es una aplicación web construida en Django que permite gestionar proyectos y las tareas asociadas a cada uno de ellos. A lo largo de este proceso de aprendizaje, se desarrollaron varias funcionalidades clave que permitieron reforzar conocimientos de desarrollo backend con Django, como la creación de vistas, manejo de formularios, manipulación de modelos y la integración con GitHub.

## Funcionalidades

- **Gestión de Proyectos:** Permite crear proyectos a los cuales se pueden asociar tareas.
- **Gestión de Tareas:** Las tareas se pueden añadir a los proyectos, y cada tarea tiene un estado (completada o no completada).
- **Acciones en Tareas:** Las tareas se pueden marcar como "hechas" o eliminarse a través de botones en la interfaz.
- **Uso de Django ORM:** Se utilizan consultas ORM para gestionar las relaciones entre proyectos y tareas, y para obtener los datos desde la base de datos.
- **Interfaz Mejorada:** La vista de tareas se presenta en una tabla HTML, permitiendo una mejor organización y presentación de las acciones para eliminar o marcar tareas como completadas.
- **Accesibilidad:** Los elementos interactivos, como los botones, tienen atributos `aria-label` para mejorar la accesibilidad.

## Tecnologías Usadas

- **Django:** Framework backend para construir la lógica y las vistas del servidor.
- **HTML5 & CSS3:** Para construir la estructura y el estilo de las vistas.
- **SQLite3:** Base de datos ligera integrada con Django para almacenar proyectos y tareas.
- **Git:** Control de versiones para seguir los cambios en el proyecto.
- **GitHub:** Repositorio remoto para guardar y compartir el código.

## Estructura del Proyecto

- **Vistas Personalizadas:** Las vistas principales son:
  - `index`: Página principal del sitio.
  - `projects`: Muestra todos los proyectos.
  - `tasks`: Lista de todas las tareas.
  - `tasksByProjNum`: Lista de tareas asociadas a un proyecto específico.
  - `create_task`: Permite crear una nueva tarea.
  - `create_project`: Permite crear un nuevo proyecto.

- **Modelo de Datos:**
  - **Project:** Almacena información básica del proyecto.
  - **Task:** Almacena el título, descripción, estado y la relación con un proyecto.

## Lecciones Aprendidas

1. **Gestión de Proyectos y Tareas con Django:** Este proyecto ha permitido explorar cómo Django gestiona modelos relacionados y cómo estructurar vistas y formularios para facilitar la interacción con esos datos.
   
2. **Uso del ORM de Django:** Manipular datos mediante consultas ORM, como filtrar tareas por proyecto, fue fundamental para gestionar adecuadamente los datos entre la base de datos y la interfaz de usuario.

3. **Despliegue del proyecto en GitHub:** Aprender a usar Git para hacer commits, crear ramas y subir el código a GitHub fue clave para el control de versiones y compartir el progreso.

## Cómo Ejecutar el Proyecto

1. **Clona este repositorio**:
   ```bash
   git clone https://github.com/usuario/mi-proyecto-django.git
   ```

2. **Instala las dependencias necesarias: Si no tienes un entorno virtual, créalo e instala Django**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate  # Windows
    pip install django
    ```

3. **Migra la base de datos**:
    ```bash
    python manage.py migrate
    ```

4. **Ejecuta el servidor**:
    ```bash
    python manage.py runserver
    ```

5. **Accede a la aplicación en tu navegador visitando: http://127.0.0.1:8000/**

## Conclusiones

Este proyecto fue una excelente oportunidad para profundizar en el desarrollo de aplicaciones web con Django. Me permitió afianzar mis habilidades en el manejo de modelos, vistas, y formularios, así como en la interacción con bases de datos. También me dio una experiencia práctica en el uso de Git y GitHub para controlar versiones y mantener el proyecto bien documentado y organizado.

## Próximos Pasos

- Agregar autenticación de usuarios: Permitir que diferentes usuarios gestionen sus propios proyectos y tareas.
- Añadir paginación: Mejorar la gestión de listas largas de tareas con paginación.
- Despliegue en un servidor real: Subir la aplicación a una plataforma como Heroku o AWS.

## Licencia

Este proyecto está bajo la licencia MIT - consulta el archivo [LICENSE](./LICENSE) para más detalles.