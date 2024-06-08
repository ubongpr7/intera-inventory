# Set the base image to Python 3.9
FROM python:3.11.0

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Run database migrations
RUN python manage.py migrate

# Expose port 8000 for the Django application
EXPOSE 8000

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

FROM python:3

# ENV PYTHONUNBUFFERED 1

# WORKDIR /app

# ADD . /app

# COPY ./requirements.txt /app/requirements.txt

# RUN pip install -r requirements.txt

# RUN python manage.py makemigrations

# RUN python manage.py migrate

# COPY . /app


