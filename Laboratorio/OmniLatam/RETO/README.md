e-commerce
It's a project part of the technical test of the company OMNILATAM

Initial setup
You must create a file in the root of the project with the name .env with the following data:

#Django
DEBUG=True
SECRET_KEY=1y1__n_j@c$g1qi9!ffq_q-bkt0+fu+25*wn=ct4*if7rq#%4&
TZ=America/Bogota    
DJANGO_SETTINGS_MODULE=reto.settings
    
#Postgres    
POSTGRES_DB=reto_db
POSTGRES_USER=reto_user
POSTGRES_PASSWORD=reto2021**.
POSTGRES_HOST=postgres    
POSTGRES_PORT=5432  
Then you must run the following command to build all the project containers:

$ make build
Finally you should generate the initial Django migrations, for them execute the following command

$ make migrate

Run project
To run the project you must execute the following command

$ make up

If you have problems connecting Django with Postgres, you should run the command: make restart CONTAINER=django

Other commands
Create a new app: make startapp NAME=example
Generate migrations: make migrate
Create a superuser: make superuser
Sort packages in the requirements.txt file
First you need to add the package to the requirements.txt file, then you run the make build command. Finally, so that the packages are ordered and with their version established in the requirements.txt file, you must execute the following command.

$ make get-requirements