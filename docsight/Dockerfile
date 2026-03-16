FROM python:3.12-slim
WORKDIR /app

# Install Python dependencies
RUN pip install --no-cache-dir flask

# Copy application files
COPY app/simple_main.py ./app/main.py

EXPOSE 8765

CMD ["python", "app/main.py"]
