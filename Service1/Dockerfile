# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory to /app
WORKDIR /app

# Copy the service1.py file into the container
COPY service1.py .

# Install any needed packages specified in requirements.txt
# If you have a requirements.txt file, uncomment the following line and copy it
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install uvicorn
# Make port 80 available to the world outside this container
EXPOSE 8001

# Define environment variable
ENV SERVICE_NAME service1

# Run service1.py when the container launches
CMD ["uvicorn", "service1:app", "--host", "0.0.0.0", "--port", "8001"]
