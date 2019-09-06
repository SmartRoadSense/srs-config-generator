FROM python:3

WORKDIR /config

ADD create-config.py /config/

RUN pip install python-dotenv

CMD [ "python", "./create-config.py" ]
