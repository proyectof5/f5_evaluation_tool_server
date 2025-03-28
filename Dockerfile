FROM python:3.12

WORKDIR /app

RUN apt-get update && apt-get install -y default-mysql-client

RUN pip install uv

COPY pyproject.toml uv.lock ./

RUN uv sync

COPY . .

ARG PORT=8000

ENV PORT=${PORT}

EXPOSE ${PORT}

CMD ["sh", "-c", "python manage.py runserver 0.0.0.0:${PORT}"]