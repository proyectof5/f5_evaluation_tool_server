FROM python:3.12

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y default-mysql-client

COPY . .

ARG PORT=8000

ENV PORT=${PORT}

EXPOSE ${PORT}

CMD ["sh", "-c", "python manage.py runserver 0.0.0.0:${PORT}"]
