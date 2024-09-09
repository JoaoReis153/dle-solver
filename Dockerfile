# Use the official Python image from the Docker Hub
FROM python:3.12.5-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install the dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Expose a port (optional, based on your application)
# EXPOSE 5000 (for example if you're using Flask, FastAPI, or Django)

# Command to run your Python application
# Replace "main.py" with your main Python file or entry point
CMD ["python", "main.py"]
