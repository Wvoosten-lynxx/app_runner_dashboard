#FROM python:3.11
#COPY . /app
#WORKDIR /app
#RUN pip install -r requirements.txt
#EXPOSE 8501
#CMD streamlit run app.py

# Use a specific lightweight Python version
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app code into the container
COPY . .

# Expose the port that Streamlit will use
EXPOSE 8080

# Set environment variables for Streamlit
ENV STREAMLIT_SERVER_PORT=8080
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0

# Start the Streamlit app
CMD ["streamlit", "run", "app.py"]