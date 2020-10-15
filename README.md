# openApi-flask
Simple REST API using OpenAPI, Flask & Connexions

# Pasos para instalar OpenApi Generator

1. Clonar el repositorio de GitHub
~~~
$ git clone https://github.com/OpenAPITools/openapi-generator.git
~~~
2. Modificar el fichero controller.mustache de python-flask

3. Run
~~~
$ mvn clean install
~~~


# openapi-generator-cli
## Docker

~~~
& git clone https://github.com/openapitools/openapi-generator
& cd openapi-generator
& sudo ./run-in-docker.sh mvn package
$ sudo ./run-in-docker.sh generate -i modules/openapi-generator/src/main/resources/specification.yml -g python-flask -o /gen/out/rules --package-name=poc_openapi.web
~~~

Una vez generado el controller, copiamos a nuestro proyecto las carpetas **models/**, **controllers/**, y ficheros **encoder.py**, **util.py** en *src/poc_openapi/web*

Creamos entorno virtual con pyenv:
~~~
$ pyenv virtualenv 3.7.2 myvenv
~~~
Entramos al entorno
~~~
$ pyenv local myvenv
~~~
Para activar desactivar entorno
~~~
$ pyenv activate <environment_name>
$ pyenv deactivate
~~~
***activate no seria necesario si tenemos configurado en el .bashrc la siguiente línea:
    __eval "$(pyenv virtualenv-init -)"__

Si fuera necesario:
~~~
pip install -r requirements.txt
~~~

y arrancamos la plataforma:
~~~
& FLASK_APP=./src/poc_openapi/run.py FLASK_DEBUG=1 flask run
~~~
