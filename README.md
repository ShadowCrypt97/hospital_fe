# syntax-team
Proyecto


exportar librerias entorno virtual
- ingresar al entorno virtual: 
.\env\Scripts\activate

- escribir: 
pip freeze > package.txt

- salimos del entorno virtual: 
deactivate  

----------------------
- al clonar el proyecto en el directorio donde está package.txt: 
virtualenv -p python3 env

- ingresar al entorno virtual: 
.\env\Scripts\activate

pip list

- instalamos todo lo que tememos en package.txt: 
pip install -r package.txt

- ingresamos a: 
cd backend

- iniciamos la api en el directorio en donde está manage.py: 
python manage.py runserver
