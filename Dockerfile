FROM python:alpine3.7 
COPY docker-api.py /app/
COPY requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt 
EXPOSE 8000 
ENTRYPOINT [ "python" ] 
CMD [ "docker-api.py" ] 