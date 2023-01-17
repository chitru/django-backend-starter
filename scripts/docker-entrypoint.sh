if [[ -f "./manage.py" ]]
then
    echo "Current folder contains manage.py"
else
    cd backend
fi

pip install --no-cache-dir --upgrade pip
pip install -r requirements.txt

python manage.py makemigrations  --noinput
python manage.py migrate --noinput

export $(grep DJANGO_SUPERUSER_USERNAME .env)
export $(grep DJANGO_SUPERUSER_PASSWORD .env)
export $(grep DJANGO_SUPERUSER_EMAIL .env)

if [ "$DJANGO_SUPERUSER_USERNAME" ]
then
    python manage.py createsuperuser \
        --noinput \
        --username $DJANGO_SUPERUSER_USERNAME \
        --email $DJANGO_SUPERUSER_EMAIL
else
    echo "Not able to create super user!!"
fi

$@


python manage.py collectstatic --noinput
python manage.py runserver 0.0.0.0:8000