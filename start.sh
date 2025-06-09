#!/bin/bash

echo "▶️ Aplicando migrações..."
python manage.py migrate

echo "🧹 Coletando arquivos estáticos..."
python manage.py collectstatic --noinput

echo "🚀 Iniciando o servidor Gunicorn..."
gunicorn Portal_de_Servicos_de_Inteligencia_de_Dados.wsgi:application --bind 0.0.0.0:$PORT
