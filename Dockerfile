FROM python:3.7-alpine

LABEL maintainer="fresnik@gmail.com"

COPY requirements.txt /

RUN pip install -r /requirements.txt

COPY src/ /app
COPY data/ikea_name_matrix_norm.json /app
WORKDIR /app

EXPOSE 4532/tcp

ENV NAME_DATA_FILE=ikea_name_matrix_norm.json

ENTRYPOINT ["python"]

CMD ["app.py"]
