# API Bancaria con Python, FastAPI, MongoDB y Docker
- ## Autor:
  Cristian Alexander Castaño Montoya
  
  [<img src="https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat&logo=linkedin">](https://www.linkedin.com/in/cristiancastano852/)

## Descripción

Esta es una API RESTful para un banco que permite a los usuarios crear cuentas bancarias y actualizar sus saldos. La API cumple con los siguientes requisitos:

- **Crear una cuenta bancaria:** Endpoint: POST /accounts.

- **Actualizar saldo de una cuenta:** Endpoint: PATCH /accounts/{account_id}. 

- **Listar todas las cuentas:** Endpoint: GET /accounts.

- **Crear un usuario:** Endpoint: POST /users. 

- **Actualizar los datos de un usuario** Endpoint: PUT /users/{user_id}.
  
- **Listar todos los usuarios:** Endpoint: GET /users. 

Entre otros endpoints que puede ser consultados en la documentación de la Api `/docs` con más detalle (Ver imagen).

  ![image](https://github.com/cristiancastano852/Api_Bancaria/assets/44209773/76682d16-f5d0-45ca-9579-72f13160f2cc)

## Principales tecnologías Utilizadas

- **Python:** Lenguaje de programación principal.
- **FastAPI:** Utilizado para crear la API RESTful.
- **Docker:** Contenedorización de la aplicación.
- **MongoDB:** Base de datos utilizada para almacenar la información de las cuentas bancarias y los usuarios.
- **GitHub Actions:** Ejecutar unit test automáticamente en cada commit.


## Instrucciones de Uso

1. Clona el repositorio desde GitHub.
2. Asegúrate de tener Docker instalado en tu sistema.
3. Ejecuta el comando `docker-compose up` en la raíz del proyecto para iniciar la aplicación.
4. **Acceder a la API:** Una vez que la aplicación esté en funcionamiento, puedes acceder a la API a través de la siguiente URL en tu navegador web:
   
    [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   
    Esto abrirá la interfaz interactiva de Swagger UI, donde puedes explorar y probar los diferentes endpoints de la API.

## Pruebas Unitarias

Se implementaron pruebas unitarias para cada uno de los endpoints utilizando la biblioteca `pytest`. El coverage alcanzado fue del **94%**, evaluado con la extensión `pytest-cov` que genera un informe detallado.
  ![image](https://github.com/cristiancastano852/Api_Bancaria/assets/44209773/edf7697c-fd08-4d6d-9adb-1c414839a526)
  
Puedes ejecutar los siguientes comandos para ejecutar las pruebas y generar el informe de cobertura:

```bash
coverage run -m pytest
coverage report -m
coverage html
```
Esto generará la carpeta htmlcov, donde encontrarás el archivo index.html. Este archivo contiene información detallada sobre la cobertura de código (Ver imagen).

## Ejecución de pruebas con GitHub Actions

Este proyecto utiliza GitHub Actions para ejecutar pruebas automáticamente en cada commit. Las pruebas se definen en el archivo `ci.yml` en el directorio `.github/workflows`. GitHub Actions se encarga de ejecutar estas pruebas en un entorno de integración continua para garantizar la integridad del código.

Puedes ver el estado de las pruebas en la pestaña "Actions" de este repositorio.

## Documentación del Código
Cada método está documentado con un **docstring** que explica qué hace cada función. Además, se añadieron comentarios en secciones específicas del código para mejorar la comprensión y mantenibilidad.

## Formato del Código

Se utilizó `autopep8` para garantizar un formato claro y consistente en todo el código.

## Arquitectura y Patrón de Diseño

**Arquitectura**

La arquitectura utilizada en este proyecto sigue el patrón Modelo-Vista-Controlador (MVC). En este patrón, los componentes se dividen en tres roles principales:

- **Modelo:** Se encarga de representar la estructura de datos y la lógica de negocio. En este proyecto, los modelos se encuentran en el directorio models/, donde cada archivo define la estructura de un modelo específico, como usuarios (user.py) o cuentas bancarias (accountBank.py).
- **Vista:** Las vistas están asociadas con las rutas de la API que devuelven respuestas al cliente (routes).
- **Controlador:** Actúa como intermediario entre las rutas (endpoints) y los servicios. Los controladores procesan las solicitudes entrantes, interactúan con los servicios para realizar operaciones comerciales y preparan la respuesta para enviarla al cliente. En este proyecto, los controladores se encuentran en el directorio controllers/.
  
La elección de la arquitectura MVC se realizó con el objetivo de seguir los principios SOLID, que promueven la modularidad, la extensibilidad y la facilidad de mantenimiento del código. La arquitectura MVC facilita la separación de responsabilidades y la organización del código en capas distintas, lo que mejora la legibilidad y la escalabilidad del proyecto.

**Patrones de desarrollo que se usarán**
- **Pattern observer**

En este proyecto, además de la arquitectura MVC, se implementara el patrón Observer para notificar a los usuarios sobre cambios en el saldo de sus cuentas bancarias. Este patrón permite una comunicación eficiente y desacoplada entre los objetos, asegurando que los usuarios sean informados sin que el componente que modifica el saldo necesite conocer los detalles de implementación de la notificación. Esto mejora la modularidad, la flexibilidad y la escalabilidad del sistema.

- **Pattern Strategy**
  
En el futuro, se espera que la API bancaria incluya funcionalidades como el cálculo de intereses y la validación de transacciones. Para manejar eficientemente estas operaciones, se aplicará el patrón Strategy. Este patrón permitirá encapsular diferentes algoritmos relacionados con el cálculo de intereses y la validación de transacciones en clases separadas. Al separar estos algoritmos, la API ganará flexibilidad y extensibilidad, ya que será posible cambiar dinámicamente la estrategia utilizada según sea necesario, sin necesidad de modificar el código existente.

## Flujo de Desarrollo Git Flow
Se planea implementar el flujo de desarrollo Git Flow en este proyecto a medida que crece y se vuelva más complejo. Actualmente, el proyecto cuenta con las ramas main y develop, pero se espera expandir este esquema a medida que se añadan más funcionalidades y se trabaje en paralelo en diferentes aspectos del proyecto.

La implementación del flujo de desarrollo Git Flow implicará:

- Crear ramas secundarias para trabajar en características específicas (Feature Branches), arreglar problemas (Hotfix Branches) y preparar lanzamientos (Release Branches).
- Utilizar Pull Requests para revisar y fusionar cambios en las ramas principales, lo que facilitará la colaboración en equipo y garantizará una mayor calidad del código.
- Realizar pruebas de integración y pruebas unitarias antes de fusionar cambios en las ramas principales.
- Documentar y mantener un registro claro de los cambios realizados en cada rama y versión del proyecto.
