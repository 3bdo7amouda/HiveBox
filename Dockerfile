FROM python:3.12-slim

# Create non-root user for security
RUN groupadd --system --gid 1001 appgroup && \
    useradd --system --uid 1001 --gid appgroup --shell /bin/false appuser

# Set working directory
WORKDIR /app

# Set environment variables
ENV FLASK_APP=app/main.py

# Copy requirements first for better layer caching
COPY requirements.txt .

# Install dependencies with pinned pip version
RUN pip install --no-cache-dir --upgrade pip==23.2.1 && \
    pip install --no-cache-dir -r requirements.txt

# Copy the Flask app with proper ownership
COPY --chown=appuser:appgroup app/ ./app/

# Switch to non-root user
USER appuser

# Expose port 5000
EXPOSE 5000

# Run the Flask app with proper signal handling
ENTRYPOINT ["python3", "-m", "flask"]
CMD ["run", "--host=0.0.0.0", "--port=5000"]