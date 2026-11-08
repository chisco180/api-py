
FROM python:3.12-slim-trixie

WORKDIR /usr/src/app

# Instalar uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Configurar ubicación del entorno virtual
ENV UV_PROJECT_ENVIRONMENT=/opt/venv

# Agregar entorno virtual al PATH
ENV PATH="/opt/venv/bin:$PATH"

# Copiar archivos de dependencias
COPY pyproject.toml uv.lock ./

# Instalar dependencias
RUN uv sync --locked --no-dev --no-install-project

# Copiar código del proyecto
COPY . .

EXPOSE 8000

# Ejecutar FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
