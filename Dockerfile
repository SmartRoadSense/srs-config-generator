FROM python:3

ADD create-config.py /

WORKDIR /

#RUN pip install python-dotenv

CMD [ "python", "./create-config.py", "config/" ]

