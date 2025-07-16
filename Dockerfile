FROM python:3.12-slim

WORKDIR /app

# Set Flask environment
ENV FLASK_APP=app/main.py

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask app
COPY app/ ./app/

# Expose port 5000
EXPOSE 5000

# Run the Flask app
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]