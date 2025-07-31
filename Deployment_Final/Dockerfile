# Use lightweight Python base image
FROM python:3.9-slim

# Set working directory inside container
WORKDIR /app

# Copy the UI app
COPY ui/app_ui.py ./app_ui.py

# Copy the requirements file
COPY requirements.txt .

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose Streamlit port
EXPOSE 8501

# Start the Streamlit app
CMD ["streamlit", "run", "app_ui.py", "--server.port=8501", "--server.address=0.0.0.0"]
