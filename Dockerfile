FROM python:3.11

FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Copia tudo primeiro
COPY . /app/

# Instala as dependências
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Torna o script start.sh executável
RUN chmod +x /app/start.sh

# Executa o start.sh no container
CMD ["/app/start.sh"]

