# Use the Python 3.9 image
FROM python:3.9

# Setup work folder
WORKDIR /backend
ADD requirements.txt /backend/

# Change work folder
#RUN mkdir /backend
#WORKDIR /backend

# Install Python dependency
RUN pip install virtualenv
RUN virtualenv venv
#RUN source venv/bin/activate
RUN . venv/bin/activate
RUN pip install django-debug-toolbar==3.2.2
RUN pip install --no-cache-dir -r requirements.txt
RUN pip3 install markdown2
#RUN pip install django-sslserver
RUN apt-get update && apt-get install -y nginx

# Copy to backend folder
COPY . /backend/
COPY nginx.conf /etc/nginx/nginx.conf
COPY ssl/fullchain.pem /etc/nginx/ssl/fullchain.pem
COPY ssl/privkey.pem /etc/nginx/ssl/privkey.pem


# Run application
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD python manage.py runsslserver 0.0.0.0:8000

