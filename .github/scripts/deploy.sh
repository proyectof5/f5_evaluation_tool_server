#!/bin/bash
set -euo pipefail

CONTAINER_NAME="local-evaluation"
IMAGE_NAME="local-evaluation:latest"
IMAGE_FILE="/root/evaluation-image.tar"

# Validación de variables de entorno requeridas
: "${DATABASE_NAME:?Falta DATABASE_NAME}"
: "${DATABASE_USER:?Falta DATABASE_USER}"
: "${DATABASE_PASSWORD:?Falta DATABASE_PASSWORD}"
: "${DATABASE_HOST:?Falta DATABASE_HOST}"
: "${DB_PORT:?Falta DB_PORT}"

echo "📦 Cargando imagen Docker desde $IMAGE_FILE..."
if [[ ! -f "$IMAGE_FILE" ]]; then
  echo "❌ Error: No se encontró la imagen $IMAGE_FILE" >&2
  exit 1
fi

docker load -i "$IMAGE_FILE"

echo "🔍 Buscando puerto usado por contenedor anterior (si existe)..."
PORT=$(docker inspect --format='{{(index (index .NetworkSettings.Ports "8000/tcp") 0).HostPort}}' "$CONTAINER_NAME" 2>/dev/null || echo "")

if [[ -z "$PORT" ]]; then
  echo "ℹ️ No se encontró puerto asignado previamente. Usando puerto por defecto: 8000"
  PORT=8000
fi

if docker ps -a --format '{{.Names}}' | grep -q "^$CONTAINER_NAME$"; then
  echo "🛑 Deteniendo y eliminando contenedor existente: $CONTAINER_NAME"
  docker stop "$CONTAINER_NAME" || echo "⚠️ Ya estaba detenido"
  docker rm "$CONTAINER_NAME"
else
  echo "ℹ️ No hay contenedor anterior con el nombre '$CONTAINER_NAME'."
fi

echo "🚀 Iniciando nuevo contenedor con puerto $PORT..."
docker run -d \
  --restart always \
  --name "$CONTAINER_NAME" \
  -p "$PORT:8000" \
  -e DATABASE_NAME="$DATABASE_NAME" \
  -e DATABASE_USER="$DATABASE_USER" \
  -e DATABASE_PASSWORD="$DATABASE_PASSWORD" \
  -e DATABASE_HOST="$DATABASE_HOST" \
  -e DB_PORT="$DB_PORT" \
  "$IMAGE_NAME"

echo "✅ Contenedor '$CONTAINER_NAME' actualizado correctamente."

echo "🧹 Limpiando imágenes huérfanas de Docker..."
docker image prune -f

echo "🗑️ Eliminando archivo de imagen temporal: $IMAGE_FILE"
rm -f "$IMAGE_FILE"
