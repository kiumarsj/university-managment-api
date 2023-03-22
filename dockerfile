FROM python:3.10-alpine
 
WORKDIR /app
 
RUN apk add --no-cache gcc musl-dev linux-headers
 
COPY requirements.txt requirements.txt
 
RUN pip install -r requirements.txt
 
EXPOSE 5000
 
COPY . .
 
CMD ["sh", "run.sh"]