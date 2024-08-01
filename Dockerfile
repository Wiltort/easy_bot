FROM python:3.12
WORKDIR /app
ADD . /usr/src/app
CMD ["python", "app.py"]

