# syntax-team
Proyecto


exportar librerias entorno virtual
- ingresar al entorno virtual => 
.\env\Scripts\activate

- escribir => 
pip freeze > package.txt

- salimos del entorno virtual => 
deactivate  

----------------------
- al clonar el proyecto en el directorio donde está package.txt => 
virtualenv -p python3 env

- ingresar al entorno virtual => 
.\env\Scripts\activate

pip list

- instalamos todo lo que tememos en package.txt => 
pip install -r package.txt

- ingresamos a => 
cd backend

- creamos la base de datos django_api y escribimos => 
python manage.py migrate

- ejecutar servidor
python manage.py runserver

- url => http://127.0.0.1:8000/api/companies/
