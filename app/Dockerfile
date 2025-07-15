FROM python:3.9-slim

WORKDIR /app

COPY version_ids_script.py .

RUN chmod +x version_ids_script.py

CMD ["python3", "version_ids_script.py"]