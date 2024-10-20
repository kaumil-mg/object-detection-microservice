FROM python:3.9-slim

WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0
    
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# Copy the application code
COPY . .

# Expose port
EXPOSE 5001

CMD ["python", "app.py"]
