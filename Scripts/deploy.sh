#!/usr/bin/env bash

# activate the virtual environment
source ~/venv/bin/activate

# Cd into the project code
cd /var/www/polling

# pull the latest codebase
git pull

# install the app dependencies
pip install -r requirements.txt

# run the databse migration
python manage.py makemigrations
python manage.py migrate

# run the collect static command
python manage.py collectstatic --no-input

# put all other commads that required for your specific app

# deactivate the virtual environment
deactivate

# reload the daemon and restart the gunicorn socket
sudo systemctl daemon-reload
sudo systemctl restart gunicorn.socket gunicorn.service
# reload nginx
sudo nginx -t && sudo systemctl restart nginx

