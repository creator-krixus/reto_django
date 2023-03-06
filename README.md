# reto_django

#Descripción
Este proyecto es una aplicación web para gestionar una lista de vulnerabilidades.
Permite a los usuarios crear, editar y eliminar nuevas vulnerabilidades.

#Requisitos
Requisitos necesarios para instalar y ejecutar este proyecto:

Python            3.10.8
Django            4.1.7
mysqlclient       2.1.1
pytest            7.2.2
pytest-django     4.5.2
requests          2.28.2
PyMySQL           1.0.2

#Instalación
Como instalar y configurar el proyecto:

1.Clona este repositorio en tu máquina local.

2.Crea un entorno virtual y actívalo:

Para windows:
py -m venv myenv
.\venv\Scripts\activate

Para Linux:
py -m venv myenv
source myenv/bin/activate

3.Instala las dependencias:
pip install -r requirements.txt

4.Crea la base de datos
py manage.py migrate

A continuación te proporciono un ejemplo de cómo crear un archivo README.md para un proyecto de Django en Python:

Nombre del proyecto
Aquí va el nombre de tu proyecto de Django.

Descripción
En esta sección, escribe una descripción breve y clara de lo que hace tu proyecto de Django. Por ejemplo:

Este proyecto es una aplicación web para gestionar una lista de tareas. Permite a los usuarios crear nuevas tareas,
marcar tareas como completadas y eliminar tareas de la lista.

Requisitos
Aquí debes mencionar los requisitos necesarios para instalar y ejecutar tu proyecto de Django. Por ejemplo:

Python 3.6 o superior
Django 3.1 o superior
PostgreSQL 12.4 o superior
Instalación
Aquí debes explicar los pasos necesarios para instalar y configurar tu proyecto de Django. Por ejemplo:

Clona este repositorio en tu máquina local.

Crea un entorno virtual y actívalo:

bash
Copy code
python3 -m venv myenv
source myenv/bin/activate
Instala las dependencias:
Copy code
pip install -r requirements.txt
Crea la base de datos:
Copy code
python manage.py migrate
Inicia el servidor de desarrollo:
Copy code
python manage.py runserver

#Uso
Para empezar a usar la API:

1.Abre un navegador web y ve a http://127.0.0.1:8000/api/v1/vulnerability/ para acceder a la página de inicio.
2.Para hacer las diferentes peticiones puedes usar postman o thunderClient
