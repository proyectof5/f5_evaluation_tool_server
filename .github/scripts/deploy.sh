#!/bin/bash
set -e

CONTAINER_NAME="local-evaluation"
IMAGE_NAME="local-evaluation:latest"

echo "📦 Cargando imagen Docker..."
docker load -i /root/evaluation-image.tar

echo "🔍 Obteniendo puerto actual asignado por Plesk..."
PORT=$(docker inspect --format='{{(index (index .NetworkSettings.Ports "8000/tcp") 0).HostPort}}' "$CONTAINER_NAME")

if [ -z "$PORT" ]; then
  echo "❌ Error: No se pudo obtener el puerto actual del contenedor '$CONTAINER_NAME'" >&2
  docker ps
  exit 1
fi

echo "🛑 Deteniendo y eliminando contenedor antiguo..."
docker stop "$CONTAINER_NAME"
docker rm "$CONTAINER_NAME"

echo "🚀 Iniciando nuevo contenedor con el mismo puerto ($PORT)..."
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

echo "✅ Contenedor actualizado correctamente con la misma configuración."

echo "🧹 Limpiando imágenes huérfanas de Docker..."
docker image prune -f

echo "🗑️ Borrando archivo de imagen temporal..."
rm -f /root/evaluation-image.tar

