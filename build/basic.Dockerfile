FROM python:3.12

RUN mkdir /run/

COPY *.py /run/

CMD [ "python3", "/run/hello.py" ]