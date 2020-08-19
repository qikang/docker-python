FROM python:3.5.9-alpine3.12

RUN pip install flask

COPY app/ /usr/src/app/

EXPOSE 80

CMD ["python","/usr/src/app/app.py"]
