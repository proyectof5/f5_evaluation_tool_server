# F5 Evaluation Tool

## Rutas principales de la API

| URL path                        | Método | Permisos | Descripción                                                        |
| ------------------------------- | ------ | -------- | ------------------------------------------------------------------ |
| /v1/competences/                | GET    | Abierto  | Lista todas las competencias                                      |
| /v1/competences/create          | POST   | Abierto  | Crea una nueva competencia                                        |
| /v1/competences/<id>/           | GET    | Abierto  | Obtiene una competencia por ID                                    |
| /v1/competences/<id>/detail     | PUT    | Abierto  | Actualiza una competencia por ID                                  |
| /v1/competences/<id>/detail     | DELETE | Abierto  | Elimina una competencia por ID                                    |
| /v1/technologies/               | GET    | Abierto  | Lista todas las tecnologías                                       |
| /v1/technologies/create         | POST   | Abierto  | Crea una nueva tecnología                                         |
| /v1/technologies/<id>/          | GET    | Abierto  | Obtiene una tecnología por ID                                     |
| /v1/technologies/<id>/detail    | PUT    | Abierto  | Actualiza una tecnología por ID                                   |
| /v1/technologies/<id>/detail    | DELETE | Abierto  | Elimina una tecnología por ID                                     |
| /v1/categories/                 | GET    | Abierto  | Lista todas las categorías                                        |
| /v1/categories/create           | POST   | Abierto  | Crea una nueva categoría                                          |
| /v1/categories/<id>/            | GET    | Abierto  | Obtiene una categoría por ID                                      |
| /v1/categories/<id>/detail      | PUT    | Abierto  | Actualiza una categoría por ID                                    |
| /v1/categories/<id>/detail      | DELETE | Abierto  | Elimina una categoría por ID                                      |
| /v1/levels/                     | GET    | Abierto  | Lista todos los niveles                                           |
| /v1/levels/create               | POST   | Abierto  | Crea un nuevo nivel                                               |
| /v1/levels/<id>/                | GET    | Abierto  | Obtiene un nivel por ID                                           |
| /v1/levels/<id>/detail          | PUT    | Abierto  | Actualiza un nivel por ID                                         |
| /v1/levels/<id>/detail          | DELETE | Abierto  | Elimina un nivel por ID                                           |

---

## Instalación

### Sin Docker

1. Instala dependencias:

   ```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
   ```
2. Realiza las migraciones si es necesario:

   ```bash
   python manage.py migrate
   ```

5. Levanta el servidor:

   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```

   - API disponible en [http://localhost:8000](http://localhost:8000)

### Con Docker

1. Crea un archivo `.env` en la raíz del proyecto partiendo del .env.example

2. Construye y levanta los servicios:

   ```bash
   docker-compose up --build
   ```

   - API disponible en [http://localhost:8010](http://localhost:8010)

---

## Test

Actualmente no hay tests automáticos definidos. Puedes agregar tests usando Django y ejecutarlos con:

```bash
python manage.py test
```

---

## Entornos

Prod: https://evaluation.coderf5.es

Dev: https://f5-evaluation-tool-server-latest.onrender.com/

