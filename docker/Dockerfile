# Use an official Python runtime as a parent image
FROM python:3.10

# Create and set the working directory
WORKDIR /app

# Clone the GitHub repository
#RUN git clone https://github.com/Miguel-Angel-Roldan-Garcia/PGPI-3.11-Motosaurio.git .
#RUN git checkout Docker
COPY . /app
RUN pip install -r requirements.txt

#WORKDIR /app/motosaurio

# Expose the port on which your Django app will run
EXPOSE 8000

WORKDIR /app/motosaurio

# Run Django migrations and collect static files (modify this based on your project)
RUN rm db.sqlite3
RUN python manage.py migrate
RUN python manage.py create_default_superuser
RUN python manage.py loaddata initial_data.json

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

