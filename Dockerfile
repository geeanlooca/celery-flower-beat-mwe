FROM python:3.11.10-alpine AS base

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt


FROM base AS celery

COPY core_processing.py .
COPY tasks.py .

FROM celery AS scheduler
COPY start_scheduler.sh .
RUN chmod +x start_scheduler.sh
ENV FLOWER_WEBUI_PORT 5555
EXPOSE ${FLOWER_WEBUI_PORT}
ENTRYPOINT [ "./start_scheduler.sh" ]

FROM celery AS worker
ENTRYPOINT [ "celery", "-A", "tasks", "worker", "-l", "info", "-E" ]