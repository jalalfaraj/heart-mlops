# Use a small Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy only requirements first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy ALL other files (app, models, etc.) into the container
COPY . .

# Run your app using Uvicorn (or update this command to whatever you use)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

