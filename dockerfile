FROM python:alpine3.8
LABEL version="1.0"

RUN adduser -D servicenow2zab

WORKDIR /home/servicenow2zab


COPY requirements.txt requirements.txt

RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app

COPY servicenow2zab.py config.py config.ini boot.sh ./
RUN chmod +x boot.sh
ENV FLASK_APP servicenow2zab.py
RUN chown -R servicenow2zab:servicenow2zab ./

USER servicenow2zab
EXPOSE 5000
ENTRYPOINT ["./boot.sh"]