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

#Uso
Para empezar a usar la API:

1.Abre un navegador web y ve a http://127.0.0.1:8000/api/v1/vulnerability/ para acceder a la página de inicio.
2.Para hacer las diferentes peticiones puedes usar postman o thunderClient
