FROM python:3.6

#Create app directory 
WORKDIR /app

#install app dependencies 
COPY requirements.txt ./

RUN pip install -r requirements.txt 

# RUN  .

#Bundle app source
COPY init  ./init
COPY wsgi.py .

EXPOSE 5000
CMD ["gunicorn"  , "--bind", "0.0.0.0:5000", "wsgi:app"]