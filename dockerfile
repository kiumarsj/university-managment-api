FROM python:3.10-alpine
 
WORKDIR /app

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache linux-headers git mariadb-dev

COPY requirements.txt requirements.txt
 
RUN pip install -r requirements.txt
 
EXPOSE 5000
 
COPY . .
 
CMD ["sh", "run.sh"]