# Use an official Python image as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Install pip manually to avoid issues with missing pip commands
RUN apt-get update && apt-get install -y \
    curl \
    && curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py \
    && python get-pip.py && rm get-pip.py \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Expose the port that Streamlit runs on
EXPOSE 8501

# Command to run the application
CMD ["streamlit", "run", "app.py"]