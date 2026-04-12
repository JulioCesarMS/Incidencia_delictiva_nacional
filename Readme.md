[![My Skills](https://skillicons.dev/icons?i=py,html,css,git,mysql,vscode)](https://skillicons.dev)

# 📁 **Project : Incidencia delictiva en México**

#![Mapa](./figures/delitos.png)


Este proyecto consiste en el desarrollo de un pipeline ETL (Extract, Transform, Load) orientado a la recopilación, procesamiento y almacenamiento de información estadística sobre delitos en México, proveniente de fuentes oficiales como el Secretariado Ejecutivo del Sistema Nacional de Seguridad Pública y el Instituto Nacional de Estadística y Geografía.


Tecnologías utilizadas:
- Python (Pandas, procesamiento de datos)
- MySQL (almacenamiento y modelado relacional)
- Docker
- Git
- Apache Airflow


# Ejecución del proyecto

- Descargar el proyecto en local : **Desktop** <break> 
- Crear un ambiente virtual  <break>
- Intalar dependencias <break> 
- Activar el ambiente virtual <break> 


 
# Estructura del Proyecto

El proyecto está estructurado de la siguiente manera:
 
  delitos_etl/
│
├── config/
│   └── settings.py
│
├── data/
│   ├── raw/              # archivos Excel originales
│   ├── processed/        # archivos limpios (opcional)
│
├── logs/
│   └── etl.log
│
├── database/
│   ├── create_table.py
│   └── mysql_client.py
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│
├── pipelines/
│   └── run_pipeline.py
│
├── dags/                 #  Airflow
│   └── delitos_dag.py
│
├── main.py
├── Dockerfile
├── Readme.md
└── requirements.txt


 # 1.- Intalación de Python y otras dependencias
 
 - Descargar Python **versión 3.12.0** e instalarlo:  `https://www.python.org/downloads/` <break> 
 - Descargar e instalar VSCode :  `https://code.visualstudio.com/ ` (Opcional)<break>
 - Descargar e instalar Git : `https://git-scm.com/downloads` <break>
 - Descargar e instalar MySQL : `https://git-scm.com/downloads` <break>
 - Descargar e instalar Docker : `https://git-scm.com/downloads` <break>

# 2.- Clonar el proyecto a una carpeta en escritorio
 
- Crear una carpeta en escritorio p.e. "BikeSharingSystem" <break> 
- Click derecho en cualquier lugar dentro de la carpeta y seleccionar **"Git Bash Here"** <break> 
- En la consola de Git ingtroducir siguiente comandos: <break> 
  - `git init` <break> 
  - `git clone https://github.com/JulioCesarMS/BikeSharingSystem` <break>
  - Esperar unos minutos a que descargue los archivos en la carpeta
  
 
# 3.- Creación de ambiente virtual

 El primer paso es ingresar al directorio (carpeta que contiene los archivos)
  - En la barra inferior de inicio de windows teclear `cmd` en el ícono **buscar**.
  - Después teclearlos siguientes comandos:
    `cd Desktop`  y enter <break>
 
    `cd BikeSharingSystem` y enter <break>
 
     **Observación**
 
     Otra opción es introducir la ruta completa, p.e. `cd Desktop/BikeSharingSystem`. Note la dirección del ícono slash `/`, si copia la ruta desde la carpeta compruebe que sea la correcta en caso contrario realizar la sustitución manualmente.
Una vez que el directorio de la consola se encuentre dentro de la carpeta ejecutar los siguientes comandos, uno a la vez,  en consola (cmd para windown o bien en terminal de linux) 
 


# Fuentes de consulta
