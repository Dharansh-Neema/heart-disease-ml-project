FROM python:3.9-slim

WORKDIR /app


COPY . /app


RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*
    
# Install core dependencies.
RUN apt-get update && apt-get install -y libpq-dev build-essential
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Streamlit runs on (default is 8501)
EXPOSE 8501


ENTRYPOINT  ["streamlit", "run", "app.py"]
