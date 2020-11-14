# PyCharm Hackathon

## Getting Started

### Without Docker

To start your frontend and backend server individually:<br>
Follow the [Backend Readme]() to setup your backend server<br>
Follow the [Frontend Readme]() to setup the frontend server<br>

### With Docker

Ensure that you have installed [Docker](https://docs.docker.com/install/) (with [Docker Compose](https://docs.docker.com/compose/install/)).

Run the development server:
```
cd <project_directory_name>
make dev-start
```

After executing `make dev-start`, you will be running:
* The application on http://localhost:8080 
* The API Server on http://localhost:8000

Make database migrations: 
```
make exec
python manage.py makemigrations
python manage.py migrate
```

Create a superuser: 
```
make exec
python manage.py createsuperuser
```

View logs of docker containers: 
```
make dev-logs
```

To stop the development server: 
```
make dev-stop
