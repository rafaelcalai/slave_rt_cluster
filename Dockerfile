# Use an official Python runtime as a parent image
FROM python:3.9

# Install necessary libs 
RUN pip install docker

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./app /app

# Run pause_unpause_container.py when the container launches
CMD ["python", "pause_unpause_container.py"]