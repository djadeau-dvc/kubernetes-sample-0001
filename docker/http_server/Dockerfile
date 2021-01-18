FROM python:3.9

WORKDIR /usr/src/app

ADD python ./python/
ADD certificates ./certificates/

WORKDIR /usr/src/app/python

CMD ["python3", "https_server.py"]