FROM fedora

# Install necessary libs 
RUN yum -y install docker
RUN dnf install python3-pip
RUN pip install docker

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./app /app

# Run pause_unpause_container.py when the container launches
CMD ["python", "pause_unpause_container.py"]