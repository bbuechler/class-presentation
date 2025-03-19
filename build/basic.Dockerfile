FROM python:3.12

RUN mkdir /app/

COPY *.py /app/

CMD [ "python3", "/app/hello.py" ]