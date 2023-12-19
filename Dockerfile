# Use an official Python runtime as a base image
FROM python:latest

# Set the working directory in the container
WORKDIR /app

# Copy the local Python script into the container at /app
COPY hello.py /app

# Run the Python program when the container starts
CMD ["python", "hello.py"]