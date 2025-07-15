FROM python:3.12-slim

WORKDIR /app

COPY version_ids_script.py .

RUN chmod +x version_ids_script.py

CMD ["python3", "version_ids_script.py"]
