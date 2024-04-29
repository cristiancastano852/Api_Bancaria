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


## Instrucciones de Uso

1. Clona el repositorio desde GitHub.
2. Asegúrate de tener Docker instalado en tu sistema.
3. Ejecuta el comando `docker-compose up` en la raíz del proyecto para iniciar la aplicación.
4. Accede a la API a través de los endpoints proporcionados.

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

## Documentación del Código
Cada método está documentado con un **docstring** que explica qué hace cada función. Además, se añadieron comentarios en secciones específicas del código para mejorar la comprensión y mantenibilidad.

## Formato del Código

Se utilizó `autopep8` para garantizar un formato claro y consistente en todo el código.

## Arquitectura y Patrón de Diseño

Arquitectura y Patrón de Diseño
La arquitectura utilizada en este proyecto sigue el patrón Modelo-Vista-Controlador (MVC). En este patrón, los componentes se dividen en tres roles principales:

- **Modelo:** Se encarga de representar la estructura de datos y la lógica de negocio. En este proyecto, los modelos se encuentran en el directorio models/, donde cada archivo define la estructura de un modelo específico, como usuarios (user.py) o cuentas bancarias (accountBank.py).
- **Vista:** Las vistas están asociadas con las rutas de la API que devuelven respuestas al cliente (routes).
- **Controlador:** Actúa como intermediario entre las rutas (endpoints) y los servicios. Los controladores procesan las solicitudes entrantes, interactúan con los servicios para realizar operaciones comerciales y preparan la respuesta para enviarla al cliente. En este proyecto, los controladores se encuentran en el directorio controllers/.
  
La elección de la arquitectura MVC se realizó con el objetivo de seguir los principios SOLID, que promueven la modularidad, la extensibilidad y la facilidad de mantenimiento del código. La arquitectura MVC facilita la separación de responsabilidades y la organización del código en capas distintas, lo que mejora la legibilidad y la escalabilidad del proyecto.
