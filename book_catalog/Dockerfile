# Start with Python slim image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy everything to /app directory
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Command to run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]