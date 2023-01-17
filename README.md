# Django-project-starter

The is a django project starter. Contains basic functionality. 

## Installation

After cloning all files and folders create a `.env` file with following details at root level.
```
# Project
PROJECT_NAME="ProjectName"
PROJECT_EMAIL="youremail@domain.com"

# Postgres
POSTGRES_DB=yourdb
POSTGRES_USER=youruser
POSTGRES_PASSWORD=yourpassword
POSTGRES_PORT=5432

# Django Administration
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=youremail@domain.com
DJANGO_SUPERUSER_PASSWORD=yourpassword

#PG Admin
PGADMIN_DEFAULT_EMAIL=root@root.com
PGADMIN_DEFAULT_PASSWORD=yourpassword

# Secret Key in base.py
SECRET_KEY=yourdjangosecretkey
```

Run `docker compose up`


- `demoapp` is an starter app that gives basic concept of django app with CRUD and token authentication.

To generate your app start with `django startapp <appname>`


# Coding Convention
I would first read Linus's coding style [Link](chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://slurm.schedmd.com/coding_style.pdf)
For HTML/CSS I would go through this [link](https://google.github.io/styleguide/htmlcssguide.html#Background)
If you are using any JS fw for frontend you can read this [link](https://github.com/ryanmcdermott/clean-code-javascript)

# Remember
- Formatting of code is done with `black` package from PyPi, Install `pip install black` and run `black {source_file_or_folder}` remember to push to main after formatting. 
