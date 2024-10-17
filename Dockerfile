# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

# Expose the port Streamlit runs on
EXPOSE 8501

# Set the command to run the Streamlit app
CMD ["streamlit", "run", "🏠 Home.py", "--server.port=8501", "--server.address=0.0.0.0"]

