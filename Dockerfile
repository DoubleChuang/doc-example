FROM python:3.9-slim

WORKDIR /app

COPY main.py /app/

RUN pip install fastapi uvicorn

ENV PORT=8080

EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]