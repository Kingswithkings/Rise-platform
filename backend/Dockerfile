FROM python:3.12-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app
RUN pip install --no-cache-dir --upgrade pip
COPY requirements/base.txt requirements/base.txt
COPY requirements/dev.txt requirements/dev.txt
RUN pip install --no-cache-dir -r requirements/base.txt
COPY . .
RUN chmod +x /app/scripts/entrypoint.sh

FROM base AS development
RUN pip install --no-cache-dir -r requirements/dev.txt
CMD ["sh", "/app/scripts/entrypoint.sh"]

FROM base AS production
CMD ["sh", "/app/scripts/entrypoint.sh"]
