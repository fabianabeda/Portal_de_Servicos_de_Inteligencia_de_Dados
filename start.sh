#!/bin/bash

echo "▶️ Aplicando migrações..."
python manage.py migrate

echo "🧹 Coletando arquivos estáticos..."
python manage.py collectstatic --noinput

echo "🚀 Iniciando o servidor Gunicorn..."
ggunicorn setup.wsgi:application --bind 0.0.0.0:$PORT

