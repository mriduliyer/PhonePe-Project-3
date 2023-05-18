# Use an appropriate base image for your API server
FROM python:3.9

# Set the working directory inside the container
WORKDIR /PhonePe-Project-3/App

# Copy the requirements file to the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the API server files to the container
COPY . .

# Expose the port on which your API server will listen
EXPOSE 5000

# Specify the command to run your API server
CMD ["python", "app.py"]