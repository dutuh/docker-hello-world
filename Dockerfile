FROM python:3.8.6-slim-buster

WORKDIR /app

COPY src .

RUN apt-get update && \
    apt-get install -y curl

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

RUN [ "chmod", "+x", "entrypoint.sh" ]

ENTRYPOINT ["entrypoint.sh"]

CMD ["python", "./app.py"]


