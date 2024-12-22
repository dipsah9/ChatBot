# Use an official Python base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

COPY .env .env

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files into the container
COPY . .

# Expose the port your Flask app runs on
EXPOSE 5000

# # Command to start the Flask app
# CMD ["python", "app.py"]

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]