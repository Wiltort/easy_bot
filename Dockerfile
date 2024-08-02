FROM python:3.10-slim
WORKDIR /app
ADD . /usr/src/app
CMD ["python", "app.py"]

