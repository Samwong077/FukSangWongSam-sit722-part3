# Start with Python slim image
FROM python:3.9-slim

# Set working directory
WORKDIR /app/inventory_management

COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy everything to /app directory
COPY . .

ENV PYTHONUNBUFFERED=1
ENV DATABASE_URL=postgresql://sit722_part3_1p7m_user:JCCM5UR0BvoCS85eeq1NoNOtwZOVy0vM@dpg-crf3hjqj1k6c73dhg9v0-a.oregon-postgres.render.com/sit722_part3_1p7m?sslmode=require

# Make port 8002 available to the world outside this container
EXPOSE 8002

# Command to run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8002"]