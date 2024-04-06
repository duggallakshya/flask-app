# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the application directory into the container
COPY ./app .

# Install any needed dependencies specified in requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 5000

# # Define environment variable
# ENV FLASK_APP=run.py

# # Run the application
# CMD ["flask", "run", "--host=http://127.0.0.1:5000/"]

CMD ["python","../run.py"]
